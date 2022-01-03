import tabula, sys

MAGIC_STRING = "1.1. Adres siedziby świadczeniodawcy: "

def create_set(pdf_path):
    dfs = tabula.read_pdf(pdf_path, stream = True, pages = 'all')
    res_list = []

    for df in dfs:
        if MAGIC_STRING in str(df.columns[0]):
            res_list.append(df.columns[0].replace(MAGIC_STRING, '').upper())
        for row in df.iterrows():
            if MAGIC_STRING in str(row[1][0]):
                res_list.append(row[1][0].replace(MAGIC_STRING, '').upper())

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
