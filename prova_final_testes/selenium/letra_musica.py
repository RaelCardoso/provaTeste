# Importação das bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)


busca = "letra de snow hey oh red hot chili peppers"


site = "https://www.google.com.br"
browser.get(site)

time.sleep(3)

browser.find_element(By.NAME, 'q').send_keys(busca)

time.sleep(3)

browser.find_element(By.NAME, 'q').send_keys(Keys.ENTER)

time.sleep(3)


try:
    div_element = browser.find_element(By.CSS_SELECTOR, 'div[jsname="WbKHeb"]')
    
    div_text = div_element.text
except Exception as e:
    div_text = "Letra não encontrada."


browser.quit()


letra_completa = div_text
print(letra_completa)
