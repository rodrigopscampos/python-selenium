from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
chrome = webdriver.Chrome(options=options)

link = 'https://www.instagram.com/neymarjr/?hl=pt-br'
chrome.get(link)

input("Pressione enter para sair")
chrome.close()
