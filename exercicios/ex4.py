#Automatize a validação de impar/par (impar_par.html)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

n = int(input('Informe um número: '))

navegador = webdriver.Chrome()
navegador.get('file:///C:/src/python-selenium/IntroducaoWeb/impar_par.html')

navegador.find_element_by_id('txt_numero').send_keys(n)
navegador.find_element_by_name('btn_processar').click()

print("Resposta: " + navegador.switch_to.alert.text)

navegador.switch_to.alert.accept()
input("Pressione Enter para fechar")
navegador.close()


