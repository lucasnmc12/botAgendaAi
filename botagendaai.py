from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as tempoPausaComputador

# Instancia o navegador
meuNavegador = webdriver.Chrome()

# Navega até a página de login
meuNavegador.get("https://www.agendaai.com.br/report")

# Aguarda até que o campo de e-mail esteja disponível para interação
email_field = WebDriverWait(meuNavegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
email_field.send_keys("taian.rosa@multimarcasconsorcios.com.br")

# Preenche a senha e faz o login
meuNavegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("TaianTaumar1!")
meuNavegador.find_element(By.XPATH, '//*[@id="send"]').send_keys(Keys.RETURN)

# Navega até a página de relatórios
WebDriverWait(meuNavegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/ul/li[4]/a'))).click()

# Seleciona a opção de período
WebDriverWait(meuNavegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="period-option"]'))).click()

# Define as datas
date_input = WebDriverWait(meuNavegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="date_start"]')))
date_input.click()
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)
date_input.send_keys("09/07/2024")

date_end_input = WebDriverWait(meuNavegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="date_end"]')))
date_end_input.click()
date_end_input.send_keys(Keys.CONTROL + 'a')
date_end_input.send_keys(Keys.DELETE)
date_end_input.send_keys("09/07/2024")

# Clica no botão "Go"
meuNavegador.find_element(By.XPATH, '//*[@id="go"]').click()

# Loop para iterar sobre as opções de filtro
for i in range(1, 15):
    WebDriverWait(meuNavegador, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="filter_schedule"]/option[{i}]'))).click()
    meuNavegador.find_element(By.XPATH, '//*[@id="send"]').send_keys(Keys.RETURN)
    tempoPausaComputador.sleep(3)
    try:
        botao_pdf = meuNavegador.find_element(By.XPATH, '//*[@id="print"]').send_keys(Keys.RETURN)
        meuNavegador.find_element(By.XPATH, '//*[@id="download"]/span').click()
        meuNavegador.find_element(By.XPATH, '//*[@id="modal-print"]/div[1]/div[2]/a[3]').click()
    except:
        pass
    

tempoPausaComputador.sleep(3)
