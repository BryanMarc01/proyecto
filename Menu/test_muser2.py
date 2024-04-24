import pymysql

def test_database_filtering(search_term):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='inscripcion',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, usuario, correo, password, rol FROM usuarios WHERE usuario LIKE %s"
            cursor.execute(sql, ('%' + search_term + '%',))
            results = cursor.fetchall()

            # Verifica que se recibieron resultados
            if results:
                print(f"Prueba exitosa: {len(results)} resultados encontrados para el término de búsqueda '{search_term}'.")
            else:
                print(f"Prueba fallida: No se encontraron resultados para el término de búsqueda '{search_term}'.")
    finally:
        connection.close()

# Llamada a la función con un término de búsqueda de ejemplo
test_database_filtering('admin')
