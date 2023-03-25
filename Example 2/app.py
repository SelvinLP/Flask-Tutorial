# Importa el módulo Flask y la función render_template
from flask import Flask, render_template 

app = Flask(__name__)  

# Agrega una ruta a la aplicación Flask. La ruta es el punto final de la URL que se usará para acceder a la página
@app.route('/')  
def home():  
    return render_template('index.html')  # Renderiza la plantilla HTML "index.html" usando la función render_template()

if __name__ == '__main__':  
    app.run()  
