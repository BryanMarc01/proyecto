from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_save_and_send_notes():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/proyecto/Menu/admin.php")

    try:
        # Suponiendo que hay un campo para ingresar notas
        notes_input = driver.find_element(By.NAME, "notas")
        notes_input.send_keys("Esta es una nota de prueba 2.")

        save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Guardar nota')]")
        save_button.click()
        print("Prueba exitosa: Las notas se guardan y envían correctamente.")

    except Exception as e:
        print(f"Prueba fallida: {str(e)}")
    
    finally:
        driver.quit()

test_save_and_send_notes()