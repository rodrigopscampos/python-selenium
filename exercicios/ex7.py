# Automatize o preenchimento do controle de estoque
# (html_css_javascript.html)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

quantidades = []

for i in range(0, 4):
    q = int(input("Quantidade do Produto {}: ".format(i+1)))
    quantidades.append(q)

navegador = webdriver.Chrome()
navegador.get(
    'file:///C:/src/python-selenium/IntroducaoWeb/html_css_javascript.html')

botoes = navegador.find_elements_by_tag_name('button')
botoes_add = [b for i, b in zip(range(0, len(botoes)), botoes) if i % 2 == 0]

for q, b in zip(quantidades, botoes_add):
    for aux in range(1, q):
        b.click()

input("Pressione Enter para fechar")
navegador.close()
