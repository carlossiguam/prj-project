from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Ruta al controlador de Firefox (geckodriver)
firefox_driver_path = '/ruta/al/geckodriver'

# Inicializa el navegador Firefox
driver = webdriver.Firefox()

# Abre la página de Google
driver.get("https://mail.emov.gob.ec")

driver.implicitly_wait(3)

# Encuentra el campo de búsqueda por su nombre

# //*[@id="username"]
search_box = driver.find_element(By.ID, "username")

# Ingresa la consulta de búsqueda
search_box.send_keys("csigua"+Keys.TAB)
#search_box.send_keys(Keys.TAB)
# //*[@id="username"]

driver.implicitly_wait(3)
search_pwd = driver.find_element(By.XPATH, '//*[@id="password"]')
# Ingresa la consulta de búsqueda
search_pwd.send_keys("R0t3n.#tomatoes")
driver.implicitly_wait(5)

search_pwd.send_keys(Keys.RETURN)

# /////////
/html/body/div[3]/div[10]/div[1]/table/tbody/tr[2]/td/ul/li[1]/div/div[2]/div[1]/span[1]
//*[@id="zlif__CLV-main__-52211__pa__0"]
# ////////



# //*[@id="zi_search_inputfield"]
# driver.implicitly_wait(5)
# search_pwd = driver.find_element(By.XPATH, '//*[@id="password"]')



# /html/body/div/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input[2]

# Envía la consulta de búsqueda presionando Enter
# search_box.send_keys(Keys.RETURN)

# Espera unos segundos para que se carguen los resultados (puedes ajustar este tiempo)
driver.implicitly_wait(5)

# Puedes realizar acciones adicionales aquí, como hacer clic en los resultados

# Cierra el navegador
# driver.quit()
