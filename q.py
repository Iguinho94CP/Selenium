from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.greatest-quotations.com/search/quotes-love.html')



elem = driver.find_elements(By.XPATH, '//*[@id="citatenrijen"]')
for el in elem:
	qlist = []
	quotations = {
	'Quotes': el.find_element(By.CLASS_NAME, 'fbquote').text,
	'Authors': el.find_element(By.CLASS_NAME, 'auteurfbnaam').text,
	'About': el.find_element(By.CLASS_NAME, 'auteur-beschrijving').text,
	'Year': el.find_element(By.CLASS_NAME, 'auteur-gebsterf').text,
	}

	qlist.append(quotations)
	print(quotations)