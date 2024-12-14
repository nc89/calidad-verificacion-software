# Usando selenium extraer el numero de usuario activos y cursos hechos de la pagina principal de -> https://campusvirtualunillanos.co/ 
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://campusvirtualunillanos.co/")

list = browser.find_elements(By.CLASS_NAME, 'h-100')
try:
    print('Numero de usuario activos ', list[0].find_element(By.TAG_NAME, 'h3').text)
    print('Cursos hechos ',list[1].find_element(By.TAG_NAME, 'h3').text)
except IndexError:
    print("No se encontraron los elementos esperados.")
except Exception as e:
    print("Ocurrió un error:", e)

browser.quit()