from selenium import webdriver
from selenium.webdriver.webkitgtk.webdriver import WebDriver

paginas_visitadas = set()
erros_encontrados = []
erros_conhecidos = [
    'This page isn’t working',
    'Esta página não está funcionando',
    'Not Found',
    'Não Encontrado'
]

chrome : WebDriver = None

def testar_pagina(pagina: str) -> None:
    chrome.get(pagina)
    paginas_visitadas.add(pagina)

    body = chrome.find_element_by_tag_name('body').text

    if len([e for e in erros_conhecidos if e in body]) > 0:
        erros_encontrados.append(pagina)
        print('PROBLEMA: {}'.format(pagina))

    links = chrome.find_elements_by_xpath('//a')

    qtd_total_links = len(links)
    print('Página: {}\nQuantidade de links:{}\n'.format(pagina, qtd_total_links))

    enderecos = [l.get_attribute('href') for l in links]
    enderecos = [e for e in enderecos if
                 e != ""
                 and e != None
                 and e not in paginas_visitadas
                 and dominio in e
                 and 'mailto:' not in e]

    enderecos = list(set(enderecos))

    i = 0
    for e in enderecos:
        i = i + 1
        print('Página {} de {}'.format(i, qtd_total_links))
        testar_pagina(e)


if __name__ == "__main__":
    raiz = input('Raiz do site (ex: "http://www.google.com.br" ): ')
    dominio = input(
        'Domínio (prefixo das págias que devem ser visitadas, ex: "google.com.br"): ')
    print('Vamos lá')

    chrome = webdriver.Chrome()

    testar_pagina(raiz)
    chrome.close()

    print('ERROS:')
    for e in erros_encontrados:
        print(e)
