import tabula, sys, re

MAGIC_STRING = "1.4. Adres zakładu leczniczego: "
MAGIC_STRING_SHORT = "1.4."
PL_ALFABET = "[A-ZĄĘŻŹŁŃÓĆŚŻ]"

# z internetow
# Function to replace multiple occurrences
# of a character by a single character
def replace_multi(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def stripms(adres):
    return adres.replace(MAGIC_STRING, '').replace(MAGIC_STRING_SHORT, '')

def simplify_address(adres):
    adres = adres.replace(MAGIC_STRING, '').replace(MAGIC_STRING_SHORT, '').upper().strip()
    adres = re.sub("\\s+", " ", adres)
    adres = replace_multi(adres, '\\.')
    adres = re.sub(PL_ALFABET + '+\\.','',adres)
    adres = adres.replace('\"', '')
    adres = adres.replace('.', '')
    adres = adres.replace('\\', ' ')
    adres = adres.replace(', ', ',')
    adres = adres.replace('/', ' ')
    adres = adres.replace('-', ' ')
    adres = re.sub("\\s+", " ", adres)
    tokeny = adres.split(',')
    if len(tokeny) > 3 and re.match("[0-9]+", tokeny[1]):
        tokeny.pop(1)
    tokeny[1] = tokeny[1].strip()
    miasto = tokeny[0]
    colon = miasto.find(':')
    if colon > -1:
        miasto = miasto[colon+1:].strip()
        tokeny[0] = miasto
    ulica = tokeny[2]
    ulica = ulica.strip()
    ul_cz = ulica.split(' ')

    for index, czesc in enumerate(ul_cz):
        if not re.match(PL_ALFABET + "+", czesc):
            if index == 0:
                ulica = ' '.join(ul_cz)
                break
            else:
                ulica = ' '.join(ul_cz[index-1:])
                break

    tokeny[2] = ulica
    adres = ','.join(tokeny)
    return adres

def create_set(pdf_path):
    dfs = tabula.read_pdf(pdf_path, stream = True, pages = 'all')
    res_list = []

    for df in dfs:
        if str(df.columns[0]).strip().startswith(MAGIC_STRING_SHORT):
            if len(stripms(df.columns[0])) > 10:
                res_list.append(simplify_address(df.columns[0]))
            else:
                res_list.append(simplify_address(df.columns[1]))
        for row in df.iterrows():
            if str(row[1][0]).strip().startswith(MAGIC_STRING_SHORT):
                if len(stripms(row[1][0])) > 10:
                    res_list.append(simplify_address(row[1][0]))
                else:
                    res_list.append(simplify_address(row[1][1]))

    return set(res_list)

def disp_results(szpitale1, szpitale2):
    szpitale_removed = szpitale1.difference(szpitale2)
    szpitale_added = szpitale2.difference(szpitale1)
    bez_zmian = szpitale1.intersection(szpitale2)

    print("Ubyło [", len(szpitale_removed), "]:")
    for szpital in szpitale_removed:
        print('[-] ', szpital)

    print("----------------------------")
    print("Przybyło [", len(szpitale_added), "]:")
    for szpital in szpitale_added:
        print('[+] ', szpital)

    print("----------------------------")
    print("Bez zmian [", len(bez_zmian), "]:")
    for szpital in bez_zmian:
        print('[o] ', szpital)


if __name__ == "__main__":
    szpitale1 = create_set(sys.argv[1])
    szpitale2 = create_set(sys.argv[2])
    disp_results(szpitale1, szpitale2)

