# Importa el módulo Flask
from flask import Flask  

# Crea una instancia de la aplicación Flask con el nombre de la aplicación como parámetro
app = Flask(__name__)  

# Agrega una ruta a la aplicación Flask. La ruta es el punto final de la URL que se usará para acceder a la página
@app.route('/')  
def home():  
    return 'Bienvenido a mi aplicación Flask!'  

# Verifica si el script se está ejecutando directamente y no importado como módulo
if __name__ == '__main__':  
    app.run() 
