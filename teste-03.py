from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
navegador = webdriver.Firefox()
wait=WebDriverWait(navegador, 10)
navegador.get("http://10.56.160.77/acesso/index2.php?")
usuario = input("Digite seu usuario")
senha = input("Digite sua senha")
navegador.find_element(By.ID,'txUsuario').send_keys(usuario)
navegador.find_element(By.ID,'txSenha').send_keys(senha)
navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/form/fieldset/table/tbody/tr[3]/td[3]/input').click()
navegador.switch_to.alert.accept()
navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/ul/ul/ul/li[2]').click()
navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/ul/ul/ul/li[2]/ul/li[1]/a').click()
while True:
    try:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'arranchar'))).click()
    except:
        break
print("Você está arranchado")