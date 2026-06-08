from flask import Flask
import psycopg2

app = Flask(__name__)

# Modificado para la Actividad 7
VERSION = "3.0.0"

@app.route("/")
def inicio():

    try:
        # Conexión a la base de datos usando los datos de tu docker-compose
        conexion = psycopg2.connect(
            host="db",
            database="empresa",
            user="admin",
            password="admin123"
        )

        cursor = conexion.cursor()

        # CAMBIO ACTIVIDAD 5: Cambiamos "SELECT version();" por la consulta a tu nueva tabla
        cursor.execute("SELECT id, nombre FROM clientes;")
        clientes = cursor.fetchall() # Trae todos los registros de la tabla clientes

        cursor.close()
        conexion.close()

        # CONSTRUCCIÓN DE LA LISTA EN HTML:
        # Convertimos los registros de la base de datos en elementos de lista <li>
        lista_html = ""
        for cliente in clientes:
            lista_html += f"<li><strong>ID:</strong> {cliente[0]} - <strong>Nombre:</strong> {cliente[1]}</li>"

        # Si la tabla está vacía, mostramos un aviso
        if not lista_html:
            lista_html = "<li>No hay clientes registrados aún.</li>"

        return f"""
        <h1>Aplicación Flask</h1>
        <h2>Versión {VERSION}</h2>
        <p style="color: green;"><strong>Conexión exitosa a PostgreSQL</strong></p>
        
        <h3>Lista de Clientes Registrados (Actividad 5):</h3>
        <ul>
            {lista_html}
        </ul>
        """

    except Exception as e:
        return f"<h1>Error de Conexión</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)