from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functools import reduce

assuntos = []

modo_grafico = not input("Deseja desabilitar modo gráfico ? (S/N): ").strip().lower() == "s"

p = ''
while True:
    p = input("Pesquisa ou Enter para terminar: ")
    fim = p.strip().lower() == ""

    if len(assuntos) > 0 and fim:
        break

    if not fim:
        assuntos.append(p)

print('Vamos lá')

options = webdriver.ChromeOptions()

if not modo_grafico:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

chrome = webdriver.Chrome(options=options)
print()

for a, i in zip(assuntos, range(0, len(assuntos))):
    print("Pesquisa {}: {}".format(i + 1, a))

    chrome.get('https://www.google.com.br')
    chrome.find_element_by_name('q').send_keys(a)
    chrome.find_element_by_name('q').send_keys(Keys.ENTER)

    knowledge_panel = chrome.find_elements_by_class_name('knowledge-panel')

    if len(knowledge_panel) == 0:
        print('Resumo não encontrado')
        continue

    description = knowledge_panel[0].find_elements_by_xpath(
        '//div[@data-attrid="description"]')

    if len(description) == 0:
        print('Resumo não encontrado')
        continue

    spans = description[0].find_elements_by_tag_name('span')
    textos = [s.text for s in spans]
    texto = reduce(lambda a, b: a if len(a) > len(b) else b, textos)

    print(texto)
    print('')

chrome.close()
