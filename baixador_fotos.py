import urllib.request
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisas = []

while True:
    p = input("Digite o tema ou Enter para continuar: ")
    continuar = p == ""

    if len(pesquisas) > 0 and continuar:
        break

    if not continuar:
        pesquisas.append(p)

print("Vamos lá")

chrome = webdriver.Chrome()

i = 0
for p in pesquisas:
    i = i + 1
    chrome.get('https://www.pexels.com')
    print("Pesquisa {}: {}".format(i, p))
    chrome.find_element_by_id('search').send_keys(p)
    chrome.find_element_by_id('search').send_keys(Keys.ENTER)

    area_fotos = chrome.find_elements_by_class_name('photos')[0]
    imgs = area_fotos.find_elements_by_xpath('//img')
    hrefs = [item.get_attribute('srcset')
             for item in imgs if item.get_attribute('srcset') != ""]

    hrefs = [h.split('?')[0] for h in hrefs]

    i = 0
    for url in hrefs[:10]:
        i = i + 1
        file_name = "output/{}_{}.png".format(p, i)
        print('Baixando\n\timagem {}\n\tPara: {}'.format(i, file_name))
        
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozilla/5.0')
        opener.retrieve(url, file_name)
        
        print()

chrome.close()
