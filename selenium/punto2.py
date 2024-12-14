# Crear 3 pestañas y navegar entre ellas con un delay de 2 segundos

from selenium import webdriver
import time
from warnings import filterwarnings

filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://github.com/")
time.sleep(1)
browser.execute_script("window.open('');")
time.sleep(1)
browser.switch_to.window(browser.window_handles[1])
time.sleep(1)
browser.get("https://facebook.com/")
browser.execute_script("window.open('');")
time.sleep(1)
browser.switch_to.window(browser.window_handles[2]) 
browser.get("https://google.com/")


time.sleep(2)
browser.switch_to.window(browser.window_handles[0]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[1]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[2]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])

browser.quit()






