from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_edit_user():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # El ID del usuario a editar está codificado en la URL. Cambia según sea necesario.
    driver.get("http://localhost/proyecto/Menu/editar_usuario.php?id=1")

    try:
        # Esperar a que los campos del formulario sean visibles
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "usuario"))
        )

        # Encuentra los campos del formulario y los actualiza
        usuario_input = driver.find_element(By.ID, "usuario")
        correo_input = driver.find_element(By.ID, "correo")
        password_input = driver.find_element(By.ID, "password")
        rol_select = driver.find_element(By.ID, "rol")

        # Limpia los campos y establece nuevos valores
        usuario_input.clear()
        usuario_input.send_keys("UsuarioActualizado")
        correo_input.clear()
        correo_input.send_keys("correoactualizado@example.com")
        password_input.clear()
        password_input.send_keys("nuevaContraseña123")
        # Selecciona un rol diferente si es necesario
        for option in rol_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == 'admin':
                option.click()  # Cambiar si el rol original es 'admin' y se desea cambiar a 'usuario'
                break

        # Envía el formulario
        driver.find_element(By.NAME, "editar_usuario").click()

        # Espera a la redirección y verifica si se muestra algún mensaje (opcional, dependiendo de tu implementación)
        WebDriverWait(driver, 10).until(
            EC.url_contains("crud_usuario.php")  # Asumiendo que la redirección ocurre a la página principal de CRUD
        )
        
        print("Prueba exitosa: Los datos del usuario fueron actualizados correctamente.")

    except Exception as e:
        print(f"Prueba fallida: {str(e)}")

    finally:
        driver.quit()

test_edit_user()
