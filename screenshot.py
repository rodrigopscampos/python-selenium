from selenium import webdriver

chrome = webdriver.Chrome()

link = 'https://www.google.com.br'
chrome.get(link)

filename = "google.png"
chrome.save_screenshot(filename)