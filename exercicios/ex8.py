#Automatize a validação de impar/par (impar_par.html)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

n = int(input('Informe um número: '))

navegador = webdriver.Chrome()
navegador.get('file:///C:/src/python-selenium/IntroducaoWeb/impar_par.html')

inputs = navegador.find_elements_by_tag_name('input')
txt_numero = inputs[0]
btn_processar = inputs[1]

#txt_numero = [el for el in inputs if el.get_attribute('type') == "text"][0]
#btn_processar = [el for el in inputs if el.get_attribute('type' == "button")][0]

txt_numero.send_keys(n)
btn_processar.click()

print("Resposta: " + navegador.switch_to.alert.text)

navegador.switch_to.alert.accept()
input("Pressione Enter para fechar")
navegador.close()


