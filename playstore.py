import sys
import csv
from selenium import webdriver

enderecos = [
    ('easynvest-RF', 'https://play.google.com/store/apps/details?id=br.com.easynvest.rendafixa'),
    ('easynvest-RV', 'https://play.google.com/store/apps/details?id=com.denke.easynvest'),
    ('terra', 'https://play.google.com/store/apps/details?id=br.com.terrainvestimentos.android'),
    ('rico', 'https://play.google.com/store/apps/details?id=br.com.rico.mobile'),
    ('XP', 'https://play.google.com/store/apps/details?id=br.com.xp.carteira'),
    ('clear', 'https://play.google.com/store/apps/details?id=br.com.clear.droid')
]

chrome = webdriver.Chrome()


def get_name():
    try:
        return chrome.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span').text
    except:
        return ''


def get_rate():
    try:
        return chrome.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/c-wiz/div[1]/div[1]').text
    except:
        return ''


def get_rateQty():
    try:
        return chrome.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/c-wiz/div[1]/span/span[2]').text
    except:
        return ''


def get_updated():
    try:
        return chrome.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[3]/div[1]/div[2]/div/div[1]/span/div/span').text
    except:
        return ''


def get_size():
    try:
        return chrome.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[3]/div[1]/div[2]/div/div[2]/span/div/span').text
    except:
        return ''


def get_installs():
    try:
        return chrome.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[3]/div[1]/div[2]/div/div[3]/span/div/span').text
    except:
        return ''


def get_currentVersion():
    try:
        return chrome.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[3]/div[1]/div[2]/div/div[4]/span/div/span').text
    except:
        return ''


def get_comments():
    try:
        elements = chrome.find_elements_by_tag_name('span')
        comments = [e.text for e in elements if e.get_attribute(
            'jsname') == 'bN97Pc']
        return comments
    except:
        return ''


result = []
for nome, e in enderecos:
    try:
        chrome.get(e)

        name = get_name()
        rate = get_rate()
        rate_qty = get_rateQty()
        updated = get_updated()
        size = get_size()
        installs = get_installs()
        current_version = get_currentVersion()
        comments = get_comments()

        result.append((nome, name, updated, size, installs,
                       current_version, rate, rate_qty, comments))
    except:
        e = sys.exc_info()[0]
        print('[' + nome + ']: ' + str(e))

chrome.close()

with open('playstore.csv', 'a+') as arquivo:
    csv_writer = csv.writer(arquivo, delimiter=";")
    for item in result:
        print(item)
        csv_writer.writerow(item)