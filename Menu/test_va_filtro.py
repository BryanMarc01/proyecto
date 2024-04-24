from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_filter_by_name_and_id():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/proyecto/Menu/admin.php")  # Cambia según sea necesario

    try:
        search_input = driver.find_element(By.ID, "buscar")
        search_input.send_keys("Ivan")  # Cambia según los datos de prueba
        search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

        # Esperar a que los resultados se actualicen y verificar la presencia de algún resultado esperado
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//tr/td[contains(text(), 'Ivan')]"))
        )
        print("Prueba exitosa: Los filtros funcionan correctamente.")
        
    except Exception as e:
        print(f"Prueba fallida: {str(e)}")
    
    finally:
        driver.quit()

test_filter_by_name_and_id()
