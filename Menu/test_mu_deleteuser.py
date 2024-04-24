from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pymysql

def test_delete_user(user_id):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"http://localhost/proyecto/menu/eliminar_usuario.php?id={user_id}")

    try:
        driver.implicitly_wait(10)  # Espera para la redirección
        current_url = driver.current_url
        assert "crud_usuario.php" in current_url
        print("Prueba de eliminación realizada con éxito en la interfaz.")
    except Exception as e:
        print(f"Error durante la prueba de eliminación: {str(e)}")
    finally:
        driver.quit()

    # Verificar en la base de datos que el usuario ha sido eliminado
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='inscripcion')
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            assert result is None
            print("Usuario correctamente eliminado de la base de datos.")
    except Exception as e:
        print(f"Error durante la verificación en la base de datos: {str(e)}")
    finally:
        connection.close()

# Ejemplo de uso: eliminando el usuario con id 1
test_delete_user(1)
