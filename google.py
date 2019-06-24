from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('https://www.google.com.br')

#preenche o campo de busca
navegador.find_element_by_name('q').send_keys('Selenium com Python')

#simula o usuário apertando a tecla enter, para ativar a busca
navegador.find_element_by_name('q').send_keys(Keys.ENTER)

#Aguarda o usuário pressionar Enter
input('Pressione enter para finalizar')

#fecha o navegador
navegador.close()