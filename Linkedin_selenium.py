from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsel import Selector
import csv

#arquivo CSV
writer = csv.writer(open('output.csv', 'w', encoding='utf-8'))
writer.writerow(['Nome','Headline','URL'])

#acessar o chrome
driver = webdriver.Chrome('/Users/Leona/Desktop/chromedriver')

#acessar o linkedin
driver.get('https://www.linkedin.com')
sleep(1)

#clicar no botao de login:
driver.find_element_by_xpath('//a[text()="Entrar"]').click()
sleep(3)
#preencher usuario:
usuario_input = driver.find_element_by_name('session_key')
usuario_input.send_keys('test@gmail.com')
sleep(2)
#preencher senha:
senha_input = driver.find_element_by_name('session_password')
senha_input.send_keys('password')

#clicar no botao de logar:
senha_input.send_keys(Keys.ENTER)
sleep(3)

#acessar o google
driver.get('https://www.google.com')
sleep(1)

#selecionar campo de busca
busca_input = driver.find_element_by_name('q')
busca_input.send_keys(Keys.ENTER)
sleep(3)

#fazer busca no google
busca_input.send_keys('site:linkedin.com/in/ AND "data scientist" AND "Rio de Janeiro"')
busca_input.send_keys(Keys.ENTER)
sleep(2)

#extrair lista de perfis
lista_perfil = driver.find_elements_by_xpath('//div[@class= "yuRUbf"]/a')
lista_perfil = [perfil.get_attribute('href') for perfil in lista_perfil]

#extrair informacao individual
for perfil in lista_perfil:
    driver.get(perfil)
    sleep(4)

    response = Selector(text=driver.page_source)
    nome = response.xpath('//title/text()').extract_first().split(" | ")
    headline = response.xpath('//h2/text()')[2].extract().strip()
    url_perfil = driver.current_url
#Tentar conectar com a pessoa
    try:
        connect = driver.find_element_by_xpath('//span[text()="Conectar"]').click()
        enviar = driver.find_element_by_xpath('//span[text()="Enviar"]').click()
    except:
        continue
    #escrever num arquivo csv
    writer.writerow([nome,headline,url_perfil])

#sair do driver
driver.quit()