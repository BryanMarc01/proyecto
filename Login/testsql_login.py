import requests

def test_sql_injection(url):
    # Datos que simulan inyecciones SQL
    payloads = [
        "' OR '1'='1",
        "admin' --",
        "' OR '1'='1' --",
        "' OR '1'='1' /*"
    ]
    
    # Datos para el formulario, cambiar según los parámetros del formulario
    data = {
        'username': 'admin',
        'password': '123'
    }
    
    # Prueba cada payload
    for payload in payloads:
        data['username'] = payload
        data['password'] = payload
        response = requests.post(url, data=data)
        
        # Aquí podrías buscar textos específicos en la respuesta que indicarían un login exitoso o un error
        if "texto_indicativo_de_error" not in response.text:
            print(f"Potencial vulnerabilidad encontrada con el payload: {payload}")
        else:
            print(f"No se encontraron vulnerabilidades con el payload: {payload}")

# URL del formulario de login
url = 'http://localhost/proyecto/Login/login.php'
test_sql_injection(url)