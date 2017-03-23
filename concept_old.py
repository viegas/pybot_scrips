from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.restinga.ifrs.edu.br/site/')


textPesq = driver.find_element_by_id('palavras')
textPesq.clear()
textPesq.send_keys('tcc')

buttomPesq = driver.find_element_by_css_selector('.ok')
buttomPesq.click()

linksPesq = driver.find_element_by_link_text('Superior')
linksPesq.click()

driver.close()
