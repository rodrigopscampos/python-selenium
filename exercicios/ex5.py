#Sem ID ou Name
#Pede um assunto e faz a pesquisa no google

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

assunto = input("Informe um assunto que deseja pesquisar: ")

navegador = webdriver.Chrome()
navegador.get('http://www.google.com.br')

navegador.find_element_by_class_name('gLFyf').send_keys(assunto)
navegador.find_element_by_class_name('gLFyf').send_keys(Keys.ENTER)

input("Pressione Enter para fechar")
navegador.close()
