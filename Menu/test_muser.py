from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_ui_filtering(search_term):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost/proyecto/Menu/crud_usuario.php")

    try:
        search_box = driver.find_element(By.NAME, "buscar")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)

        results = driver.find_elements(By.XPATH, "//tr[contains(@style, 'background-color: #FFCC00;')]/td[2]")
        if results:
            print(f"Prueba exitosa: Encontrados {len(results)} resultados en la interfaz de usuario para el término '{search_term}'.")
        else:
            print(f"Prueba fallida: No se encontraron resultados en la interfaz de usuario para el término '{search_term}'.")

    finally:
        driver.quit()

# Llamada a la función con un término de búsqueda de ejemplo
test_ui_filtering('admin')
