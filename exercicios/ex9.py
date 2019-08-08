#Colete todos os links da página “favoritos.html”

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get('file:///C:/src/python-selenium/IntroducaoWeb/favoritos.html')


el_links = navegador.find_elements_by_tag_name('a')
links = [l.get_attribute('href') for l in el_links]

for item in links:
    print(item)

print()
input("Pressione Enter para fechar")
navegador.close()