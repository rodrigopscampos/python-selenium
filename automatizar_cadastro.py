

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def log_status(texto):
    print("STATUS: " + str(texto))

def log_erro(texto):
    print("ERRO: " + str(texto))
    #f = open('erros.txt', 'a')
    #f.write(texto)

def log_success(texto):
    print("SUCESSO: " + str(texto))

SEPARADOR = ";"

navegador = webdriver.Chrome()

navegador.get("file:///C:/src/python-selenium/cadastro.html")

f = open('cadastro.csv', 'r', encoding='utf8')

cabecalho = True
i = 0
for linha in f:
    i+=1
    log_status("Linha " + str(i))

    if cabecalho:
        cabecalho = False
        continue

    colunas = linha.split(SEPARADOR)
    #Nome;Sobrenome;Email;Endereço;Complemento;Pais;Estado;CEP;SEXO;Aceito_Termos_Contrato;Aceito_Dados_Roubados;Arquivo
    nome = colunas[0]
    sobrenome = colunas[1]
    email = colunas[2]
    endereco = colunas[3]
    complemento = colunas[4]
    pais = colunas[5]
    estado = colunas[6]
    cep = colunas[7]
    sexo = colunas[8]
    aceito_termos_contrato = colunas[9]
    aceito_dados_roubados = colunas[10]
    end_arquivo = colunas[11]

    navegador.find_element_by_id('firstName').send_keys(nome)
    navegador.find_element_by_id('lastName').send_keys(sobrenome)
    navegador.find_element_by_id('email').send_keys(email)
    navegador.find_element_by_id('address').send_keys(endereco)
    navegador.find_element_by_id('address2').send_keys(complemento)

    [opc for opc in navegador.find_elements_by_xpath("//select[@id='country']/option") 
        if opc.text.upper() == pais.upper()][0].click()

    [opc for opc in navegador.find_elements_by_xpath("//select[@id='state']/option") 
        if opc.text.upper() == estado.upper()][0].click()

    navegador.find_element_by_id('zip').send_keys(cep)

    act = webdriver.ActionChains(navegador)
    if sexo.upper() == "M":
        act.move_to_element(navegador.find_element_by_id('gender_m')).click().perform()
    elif sexo.upper() == "F":
        act.move_to_element(navegador.find_element_by_id('gender_f')).click().perform()
    else:
        log_erro("Valor de sexo inválida: {}. Por padrão, vamos assumir M".format(sexo))
        act.move_to_element(navegador.find_element_by_id('gender_m')).click().perform()
    
    if aceito_termos_contrato.upper() == "S" or aceito_termos_contrato.upper() == "Y":
        act = webdriver.ActionChains(navegador)
        act.move_to_element(navegador.find_element_by_id('accept-terms'))
        act.click().perform()

    if aceito_dados_roubados.upper() == "S" or aceito_dados_roubados.upper() == "Y":
        act = webdriver.ActionChains(navegador)
        act.move_to_element(navegador.find_element_by_id('steal-data'))
        act.click().perform()

    try:
        navegador.find_element_by_id('document').send_keys(end_arquivo)
    except:
        log_erro(end_arquivo)

    navegador.find_element_by_xpath('//button').click()

    log_success(nome + ": " + navegador.switch_to.alert.text)
    navegador.switch_to.alert.accept()

    navegador.back()
    navegador.refresh()
    #input("Pressione Enter para continuar")