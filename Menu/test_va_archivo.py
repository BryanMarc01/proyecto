from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_view_files_button():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/proyecto/Menu/admin.php")

    try:
        view_files_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Ver archivos')]")
        view_files_button.click()

        # Verificar que el contenido se muestra correctamente
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "tabcontent"))
        )
        print("Prueba exitosa: El contenido de los archivos se muestra correctamente.")
        
    except Exception as e:
        print(f"Prueba fallida: {str(e)}")
    
    finally:
        driver.quit()

test_view_files_button()
