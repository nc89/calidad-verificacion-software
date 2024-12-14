# Usando selenium llevar y enviar el siguiente formulario -> http://demo.guru99.com/test/login.html
import time
from warnings import filterwarnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


filterwarnings("ignore")
browser = webdriver.Chrome()
browser.get("https://demo.guru99.com/test/login.html")
formEmail = browser.find_element(By.ID, "email")
formEmail.clear()
formEmail.send_keys('admin')

formPasswd = browser.find_element(By.ID, "passwd")
formPasswd.clear()
formPasswd.send_keys('admin123')

submitButton = browser.find_element(By.ID, 'SubmitLogin')
submitButton.send_keys(Keys.ENTER)

print("\nCerrando navegador...")
time.sleep(4)
browser.quit()



