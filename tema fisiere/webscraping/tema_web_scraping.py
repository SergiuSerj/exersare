import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://bnr.ro/Cursul-de-schimb-524.aspx')
# print(type(req))
link = BeautifulSoup(req.text, 'html.parser')   #html.parser, html5lib
# print(link)  #sursa paginii

main = link.find_all('div', attrs={'id': 'contentDiv'})
# print(main)

header_list = []
dataset = []
for obj in main:
    for table_idx in obj.find_all('table'):
        # print(table_idx)
        for table_trs in table_idx.find_all('tr'):
            # print(table_trs, '-----------------------')
            if table_trs.find_all('th'):
                # header_list = [header_data.get_text() for header_data in table_trs.find_all('th')]
                for header_data in table_trs.find_all('th'):
                    if header_data.get_text() != '':
                        header_list.append(header_data.get_text())
            list_with_tr = []
            for idx, td in enumerate(table_trs.find_all('td')):
                if idx == 0:
                    list_with_tr.append(td.get_text().strip())
                else:
                    if td.get_text().strip() != '':
                        list_with_tr.append(td.get_text().replace(',', '.'))
            if list_with_tr:
                dataset.append(list_with_tr)

# header_list.append()
if " " in header_list:
    header_list.remove(" ")
header_list[0].append(" ")

print(header_list)
# del dataset[0]
# print(dataset)

df = pd.DataFrame(dataset, columns=header_list)
print(df)
df.to_excel("Curs_BNR_test.xlsx", index=False)

# pip install xlwt        ptr fisiere .xls
# pip install openpyxl    ptr fisiere .xlsx

# https://bnr.ro/Cursul-de-schimb-524.aspx link ptr tabelul BNR folosit la tema