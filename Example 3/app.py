from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [  
    {'id': 1, 'name': 'Juan', 'email': 'juan@mail.com'},
    {'id': 2, 'name': 'Maria', 'email': 'maria@mail.com'},
    {'id': 3, 'name': 'Pedro', 'email': 'pedro@mail.com'}
]

@app.route('/') 
def index():
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':  
        name = request.form['name'] 
        email = request.form['email'] 
        new_id = users[-1]['id'] + 1  # Obtiene el id del nuevo usuario
        # Agrega un nuevo usuario a la lista de usuarios
        users.append({'id': new_id, 'name': name, 'email': email})
        # Redirige al usuario a la página de inicio
        return redirect(url_for('index'))
    else:
        # Si no se envió un formulario con el método POST, renderiza la plantilla HTML para agregar un usuario
        return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])  
def edit(id):
    user = next((u for u in users if u['id'] == id), None)  # Busca un usuario por su id
    if user is None:  # Si no se encontró el usuario, redirige al usuario a la página de inicio
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form['name']  
        email = request.form['email']  
        user['name'] = name  
        user['email'] = email 
        # Redirige al usuario a la página de inicio
        return redirect(url_for('index'))
    else:
        # Si no se envió un formulario con el método POST, renderiza la plantilla HTML para editar un usuario
        return render_template('edit.html', user=user)

@app.route('/delete/<int:id>')  # Define una ruta para la página de eliminar un usuario
def delete(id):
    user = next((u for u in users if u['id'] == id), None)  # Busca un usuario por su id
    if user is not None:  # Si se encontró el usuario
        users.remove(user)  # Elimina el usuario de la lista de usuarios
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)  # Inicia la aplicación en modo de depuración
