import sqlite3
from flask import Flask, render_template, flash, request, redirect, url_for, session, send_file, current_app, g, make_response
from flask_wtf.recaptcha import fields
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import socket
import os
import re
from form import Fields

app = Flask(__name__)
app.secret_key = 'tolo'

@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        return redirect(session['homepage'])
    return render_template("index.html")


@app.route('/login', methods=('GET', 'POST'))
def login():
    if 'username' in session:
        return redirect(session['homepage'])
    if request.method == 'POST': 
        username = request.form['user']
        password = request.form['password']
        if username == '':
            flash('Por favor diligencia todos los campos')
            return render_template('index.html')
        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()
        user = cursor.execute("SELECT * FROM empleado WHERE nombre_usuario = ? AND password = ?", (username, password)).fetchone()
        print (user)
        

        if user is None:
            mensaje="No se encontró el usuario"
            flash(mensaje)
            return render_template('index.html')
        else:
            sesskey = os.urandom(5)
            session['id'] = user[10]
            session['sesskey'] = g.sesskey #Abreviación de "session key"
            session.update({'username':username})
            session['sessaddr'] = request.remote_addr

            if user[10] == 1:
                #Con esta linea guardamos la página principal de cada usuario, nos ayuda a redirigir al usario en caso de que tenga una sesión activa y quiera ingresar nuevamente a login. 
                session['homepage'] = url_for('loginSuperadmin') 
                return redirect(url_for('loginSuperadmin'))

            elif user[10] == 2: 
                session['homepage'] = url_for('loginAdmin')
                return redirect(url_for('loginAdmin'))

            elif user[10] ==3:
                session['homepage'] = url_for('loginEmployee')
                return redirect(url_for('loginEmployee')) 

    return render_template('index.html')

@app.route('/login/superadmin', methods=('GET', 'POST'))
def loginSuperadmin():
    return redirect(url_for('dashboard'))

@app.route('/login/admin', methods=('GET', 'POST'))
def loginAdmin():
    if 'username' in session and session['id'] == 2 and session['sesskey'] == g.sesskey:
        print(session['sesskey'])
        return render_template('view_admin.html')
    return redirect(url_for('index'))

@app.route('/login/employee', methods=('GET', 'POST'))
def loginEmployee():
    return render_template('user_employee.html')

@app.route('/superadmin/dashboard/')
def dashboard():
    if 'username' not in session:
        return index()
    print(session)
    g.tolo = 'test'
    print(g.tolo)
    return render_template('dashboard.html')

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


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    print(g.tolo)
    session.clear()
    return redirect(url_for('index'))
app.run(debug=True, host=f'{socket.gethostbyname(socket.gethostname())}')