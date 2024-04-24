from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def test_data_exposure():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/proyecto/estudiante.php")  

    try:
        # Llenar el formulario con datos que podrían causar errores de SQL
        driver.find_element(By.ID, "nombre").send_keys("' OR '1'='1")
        driver.find_element(By.ID, "email").send_keys("test@example' OR '1'='1.com")
        driver.find_element(By.NAME, "submit").click()

        # Esperar y verificar que no se muestren mensajes de error que contengan información técnica
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        body_text = driver.find_element(By.TAG_NAME, "body").text
        assert "SQL" not in body_text and "Exception" not in body_text and "Error:" not in body_text
        print("Prueba exitosa: No se expone información técnica en mensajes de error.")
        
    except Exception as e:
        print(f"Prueba fallida: {str(e)}")
    
    finally:
        driver.quit()

test_data_exposure()
