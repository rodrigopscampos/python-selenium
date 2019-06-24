from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.buscape.com.br/smartphone-motorola-moto-g-7-plus-xt1965-64gb'
#url = 'https://www.buscape.com.br/smartphone-apple-iphone-x-64gb'
#url = 'https://www.buscape.com.br/dell-inspiron-14-5000-5481-m10-2-em-1-intel-core-i3-8145u-2-1-ghz-4096-mb-1024-gb'

options = webdriver.ChromeOptions()

modo_grafico = input("Habilitar modo gráfico ? (S/N): ") == "S"

if not modo_grafico:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

chrome = webdriver.Chrome(options=options)
chrome.implicitly_wait(10) #segundos

chrome.get(url)
chrome.maximize_window()

menor_preco = chrome.find_element_by_xpath("//li[contains(.,'menor preço')]")
act = webdriver.ActionChains(chrome)
act.move_to_element(menor_preco).click().perform()
print("Ordenação 'Menor Preço' selecionada")
time.sleep(2)

#scroll
body = chrome.find_element_by_tag_name('body')
for i in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

ofertas = chrome.find_elements_by_xpath("//div[@class='product-offers']/div/li")
print('{} ofertas encontradas'.format(len(ofertas)))

dados = []
tentativa = 1
while len(dados) == 0:
    print('Tentativa ' + str(tentativa) )
    for o in ofertas:
        vendedor = o.find_element_by_class_name('offer__seller').find_element_by_tag_name('img').get_attribute('alt')
        preco_vista = o.find_element_by_class_name('featured-price').find_element_by_tag_name('span').text
        preco_prazo_campos = o.find_elements_by_class_name('secondary-price')
        preco_prazo_campos = [x.text for x in preco_prazo_campos]
        preco_prazo = " ".join(preco_prazo_campos)

        dados.append([vendedor, preco_vista, preco_prazo])

    if "Carregando" in [x[0] for x in dados]:
        dados = []
        tentativa = tentativa + 1
        time.sleep(1)

print('DADOS:')
for d in dados:
    print(d)

chrome.close()
print('fim')