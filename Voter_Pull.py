import requests

def pull_district(num):
    URL = f'https://www6.ohiosos.gov/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:{num}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101Firefox/50.0'}
    source=requests.get(URL, headers=headers).text
    with open(f'District_{num}.txt', 'w') as file_object:
        file_object.write(source)
for i in range(1,5):
    pull_district(i)