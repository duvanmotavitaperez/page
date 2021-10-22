import sqlite3
from flask import Flask, render_template, flash, request, redirect, url_for, session, send_file, current_app, g, make_response
from werkzeug.utils import secure_filename
import os 

app = Flask(__name__)
app.secret_key = os.urandom( 24 )

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method=='POST':

        username = request.form['user']
        password = request.form['password']

        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()

        user = cursor.execute("SELECT * FROM empleado WHERE nombre_usuario = ? AND password = ?", (username, password)).fetchone()

        print (user)

        if user is None:
            mensaje="No se encontro el usuario"
            flash(mensaje)
            return render_template('index.html', mensaje=mensaje)
            

        else:

            if user[10] == 2:
                
                return loginAdmin()

            elif user[10] ==3:

                return loginEmploye()

            elif user[10] == 1:
                
                return loginSuperadmin()

    else: 

        return render_template('index.html')

@app.route('/login/superadmin', methods=('GET', 'POST'))
def loginSuperadmin():
    return render_template('dashboard.html')

@app.route('/login/employee', methods=('GET', 'POST'))
def loginEmploye():
    return render_template('user_employee.html')

@app.route('/login/admin', methods=('GET', 'POST'))
def loginAdmin():
    return render_template('view_admin.html')
           

@app.route('/admin/addemployee/', methods=('GET', 'POST'))
def adminAdd():
    return render_template('add_employee.html')

@app.route('/admin/addemployee/new', methods=('GET', 'POST'))
def adminAddnew():

    if request.method=='POST':

        name = request.form['name']
        cedula = request.form['cedula']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        genero = request.form['genero']
        contrasena = request.form['contrasena']
        usuario = request.form['usuario']
        correo = request.form['correo']
        admision = request.form['admision']
        contract = request.form['contract']
        contract_end = request.form['contract_end']
        dependencia = request.form['dependencia']
        salary = request.form['salary']
        rol = request.form['rol']
      

        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()

        cursor.execute("INSERT INTO contrato values (?, ?, ?, ?)", (contract, admision, contract_end, salary))
        cursor.execute("INSERT INTO empleado (nombre, cedula, genero, password, direccion, telefono, correo, contrato_id, dependencia_id, rol_id, nombre_usuario) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, cedula, genero, contrasena, direccion, telefono, correo, contract, dependencia, rol, usuario))

        con.commit()
        con.close()
    return render_template('add_employee_new.html', name=name, cedula=cedula, dependencia=dependencia, usuario=usuario)

@app.route('/admin/findemployee')
@app.route('/admin/findemployee/<int:id>')
def adminFind(id=None):
    return render_template('find_employee.html')

@app.route('/admin/Editemploye/')
def adminEdit():
    return render_template('edit_employee.html')

@app.route('/admin/deleteEmployee/')
@app.route('/superadmin/deleteEmployee/')
def adminDelete():
    return render_template('delete_employee.html')

@app.route('/superadmin/dashboard/')
def dashboard():
    return render_template('dashboard.html')

app.run(debug=True, host='127.0.0.1', port=5000)
