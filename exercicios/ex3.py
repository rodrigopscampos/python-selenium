# Automatize o preenchimento do controle de estoque (html_css_javascript.html)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

quantidades = []

for i in range(0, 4):
    q = int(input("Quantidade do Produto {}: ".format(i+1)))
    quantidades.append(q)

navegador = webdriver.Chrome()
navegador.get(
    'file:///C:/src/python-selenium/IntroducaoWeb/html_css_javascript.html')


i = 0
for q in quantidades:
    for aux in range(1, q):
        navegador.find_element_by_id('btn_{}_add'.format(i+1)).click()
    i += 1

input("Pressione Enter para fechar")
navegador.close()
