from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def test_create_user():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/proyecto/Menu/ManUsuario.php")  # Ajusta esta URL según sea necesario

    try:
        usuario = driver.find_element(By.NAME, "usuario")
        password = driver.find_element(By.NAME, "password")
        password2 = driver.find_element(By.NAME, "password2")
        correo = driver.find_element(By.NAME, "correo")

        usuario.send_keys("Peter")
        password.send_keys("123")
        password2.send_keys("123")
        correo.send_keys("peter@gmail.com")

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-info.btn-block[type='submit']"))
        )
        submit_button.click()

        # Verificación de los mensajes de error o de éxito
        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger"))
            )
            print(f"Prueba fallida: {error_message.text}")
        except TimeoutException:
            print("Prueba exitosa: No se encontraron mensajes de error, el usuario fue creado correctamente.")

    except NoSuchElementException as e:
        print(f"Elemento no encontrado: {str(e)}")
    except TimeoutException as e:
        print(f"La operación ha excedido el tiempo de espera: {str(e)}")
    except Exception as e:
        print(f"Prueba fallida: {str(e)}")

    finally:
        driver.quit()

test_create_user()
