from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el driver de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abre la página del formulario de login
driver.get("http://localhost/proyecto/Login/login.php")

# Encuentra los campos del formulario
username_input = driver.find_element(By.NAME, 'usuario')
password_input = driver.find_element(By.NAME, 'password')

# Limpia cualquier dato previo en los campos (por si acaso)
username_input.clear()
password_input.clear()

# Prueba con entradas válidas
username_input.send_keys("")
password_input.send_keys("")
password_input.send_keys(Keys.RETURN)

try:
    # Espera hasta 10 segundos hasta que la URL cambie a la página de inicio después del login
    WebDriverWait(driver, 10).until(EC.url_contains("http://localhost/proyecto/Menu/"))

    print("Login exitoso: Has sido redirigido a la página principal.")
except TimeoutException:
    print("Login fallido: No se encontro el mensaje de exito.")

# Cierra el navegador
driver.quit()
