from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
   
def test_form_submission():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/proyecto/estudiante.php")  

    try:
        # Llenar campos de texto
        driver.find_element(By.ID, "nombre").send_keys("Juan")
        driver.find_element(By.ID, "apellido").send_keys("Pérez")
        driver.find_element(By.ID, "email").send_keys("juan.perez@example.com")
        driver.find_element(By.ID, "telefono").send_keys("8095551234")
        driver.find_element(By.ID, "direccion").send_keys("Calle Ejemplo 123")

        # Cargar archivos
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        driver.find_element(By.ID, "formulario").send_keys(os.path.join(base_path, "test_formulario.pdf"))
        driver.find_element(By.ID, "foto").send_keys(os.path.join(base_path, "test_foto.pdf"))
        driver.find_element(By.ID, "acta_nacimiento").send_keys(os.path.join(base_path, "test_acta.pdf"))
        driver.find_element(By.ID, "certificacion_bachiller").send_keys(os.path.join(base_path, "test_certificacion.pdf"))
        driver.find_element(By.ID, "record_calificaciones").send_keys(os.path.join(base_path, "test_record.pdf"))
        driver.find_element(By.ID, "certificado_salud").send_keys(os.path.join(base_path, "test_salud.pdf"))
        driver.find_element(By.ID, "cedula_identidad").send_keys(os.path.join(base_path, "test_cedula.pdf"))

        # Enviar el formulario
        driver.find_element(By.NAME, "submit").click()

        # Verificar que el formulario fue enviado correctamente
        WebDriverWait(driver, 10).until(
            EC.url_contains("procesar_inscripcion.php")  # Asumiendo que la redirección ocurre a la página principal de CRUD
        )
        print("Prueba exitosa: El formulario de inscripción ha sido enviado correctamente.")
        
    except Exception as e:
        print(f"Prueba fallida: {str(e)}")
    
    finally:
        driver.quit()

test_form_submission()
