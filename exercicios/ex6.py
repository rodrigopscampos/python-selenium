# Clique em ver a hora e imprima a hora informada (javascript.html)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

navegador.get('file:///C:/src/python-selenium/IntroducaoWeb/javascript.html')

navegador.find_elements_by_tag_name('button')[1].click()
hora = navegador.find_element_by_tag_name('span').text

print("Hora: " + str(hora))
input("Pressione Enter para fechar")
navegador.close()
