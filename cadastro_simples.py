from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get('file:///C:/src/python-selenium/cadastro.html')

chrome.find_element_by_id('firstName').send_keys('Rodrigo')
chrome.find_element_by_id('lastName').send_keys('Campos')
chrome.find_element_by_id('address').send_keys('Av. Abc')
chrome.find_element_by_id('address2').send_keys('Apto 123')

[p for p in chrome.find_elements_by_xpath("//select[@id='country']/option") if p.text == "Brasil"][0].click()
[e for e in chrome.find_elements_by_xpath("//select[@id='state']/option") if e.text == "São Paulo"][0].click()

chrome.find_element_by_id('zip').send_keys('00000-000')

act = webdriver.ActionChains(chrome)
act.move_to_element(chrome.find_element_by_id('gender_f')).click().perform()

act = webdriver.ActionChains(chrome)
act.move_to_element(chrome.find_element_by_id('steal-data'))
act.click().perform()

chrome.find_element_by_id('document').send_keys(r'C:\src\python-selenium\cadastro_simples.py')

chrome.find_element_by_xpath('//button').click()
alert = chrome.switch_to.alert

print('resultado: {}'.format(alert.text))
alert.accept()

chrome.switch_to.default_content
chrome.back()

input('Pressione enter para finalizar')
chrome.close()  