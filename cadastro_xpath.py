from selenium import webdriver
import time

chrome = webdriver.Chrome()

chrome.get('file:///C:/src/python-selenium/cadastro.html')

chrome.find_element_by_xpath("//label[contains(.,'Nome')]/following-sibling::input[1]").send_keys('Rodrigo')
chrome.find_element_by_xpath("//div[contains(., 'Sobrenome é requerido')]/preceding-sibling::input[1]").send_keys('Campos')


chrome.find_element_by_xpath("//label[contains(.,'Endereço')]/following-sibling::input[1]").send_keys('Av. Abc')
chrome.find_element_by_xpath("//label[contains(.,'Complemento')]/following-sibling::input[1]").send_keys('Apto 123')

[p for p in chrome.find_elements_by_xpath("//select[@id='country']/option") if p.text == "Brasil"][0].click()
[e for e in chrome.find_elements_by_xpath("//select[@id='state']/option") if e.text == "São Paulo"][0].click()

chrome.find_element_by_xpath("//label[contains(.,'CEP')]/following-sibling::input[1]").send_keys('00000-000')

act = webdriver.ActionChains(chrome)
act.move_to_element(chrome.find_element_by_id('gender_f')).click().perform()

act = webdriver.ActionChains(chrome)
act.move_to_element(chrome.find_element_by_id('steal-data'))
act.click().perform()

chrome.find_element_by_xpath("//input[@type='file'][1]").send_keys(r'C:\src\python-selenium\cadastro.py')

chrome.find_element_by_xpath('//button').click()
chrome.switch_to.alert.accept()

chrome.save_screenshot('cadastro.png')
time.sleep(1)

chrome.back()