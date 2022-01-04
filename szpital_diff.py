import tabula, sys, re

MAGIC_STRING = "1.1. Adres siedziby świadczeniodawcy: "
PL_ALFABET = "[A-ZĄĘŻŹŁŃÓĆ]"

# z internetow
# Function to replace multiple occurrences
# of a character by a single character
def replace_multi(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def simplify_address(adres):
    adres = adres.replace(MAGIC_STRING, '').upper()
    adres = replace_multi(adres, ' ')
    adres = replace_multi(adres, '\\.')
    adres = re.sub(PL_ALFABET + '+\\.','',adres)
    adres = adres.replace('\"', '')
    adres = adres.replace('.', '')
    adres = adres.replace('\\', ' ')
    adres = replace_multi(adres, ' ')
    tokeny = adres.split(',')
    tokeny.pop(1)
    ulica = tokeny[2]
    ul_cz = ulica.split(' ')

    for index, czesc in enumerate(ul_cz):
        if not re.match(PL_ALFABET + "+", czesc):
            if index == 0:
                ulica = ' '.join(ul_cz)
            else:
                ulica = ' '.join(ul_cz[index-1:])

    tokeny[2] = ulica
    adres = ','.join(tokeny)
    adres = adres.replace(', ', ',')
    adres = adres.replace('/', ' ')
    adres = adres.replace('-', ' ')
    adres = adres.replace('\\', ' ')
    adres = replace_multi(adres, ' ')
    return adres

def create_set(pdf_path):
    dfs = tabula.read_pdf(pdf_path, stream = True, pages = 'all')
    res_list = []

    for df in dfs:
        if MAGIC_STRING in str(df.columns[0]):
            res_list.append(simplify_address(df.columns[0]))
        for row in df.iterrows():
            if MAGIC_STRING in str(row[1][0]):
                res_list.append(simplify_address(row[1][0]))

    return set(res_list)


szpitale1 = create_set(sys.argv[1])
szpitale2 = create_set(sys.argv[2])

szpitale_removed = szpitale1.difference(szpitale2)
szpitale_added = szpitale2.difference(szpitale1)

print("Ubyło [", len(szpitale_removed), "]:")
for szpital in szpitale_removed:
    print('[-] ', szpital)

print("----------------------------")
print("Przybyło [", len(szpitale_added), "]:")
for szpital in szpitale_added:
    print('[+] ', szpital)
