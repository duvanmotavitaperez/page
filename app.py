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
        print(type(user))
        print (user)

        if user is None:
            mensaje="No se encontro el usuario"
            flash(mensaje)
            con.close() 
            return render_template('index.html', mensaje=mensaje)
         
        
        else:

            if user[10] == 2:
                
                return loginAdmin()
                

            elif user[10] ==3:

                return loginEmploye()

            elif user[10] == 1:
                
                return loginSuperadmin()
        con.close() 
    else: 

        return render_template('index.html')

@app.route('/login/superadmin', methods=('GET', 'POST'))
def loginSuperadmin():
    return render_template('dashboard.html')

@app.route('/login/employee', methods=('GET', 'POST'))
def loginEmploye():

    if request.method == 'POST':

        username = request.form['user']

        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM empleado WHERE nombre_usuario = ?", (username, )).fetchone
        for row in cursor:
            print(row) 
        
        cursor.execute("SELECT * FROM contrato WHERE contrato_id = ?", (row[8],)).fetchone

        for rw in cursor:
            print(rw) 

        cursor.execute("SELECT * FROM dependencia WHERE dependencia_id = ?", (row[9],)).fetchone

        for rw2 in cursor:
            print(rw2)

        return render_template('user_employee.html', nombre=row[1], id=row[0], direccion=row[5], telefono=row[6], inicio=rw[1], contrato=row[8], fin=rw[2], dependencia=rw2[1], salario=rw[3])
              
    else:
        return render_template('user_employee.html')


@app.route('/login/employee/feed', methods=('GET', 'POST'))
def feed():

    if request.method == 'POST':

        mes = request.form['Mes']
        username = request.form['id']

        print(username)

        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM empleado WHERE empleado_id = ?", (username, )).fetchone
        for row1 in cursor:
            print(row1) 
        
        cursor.execute("SELECT * FROM contrato WHERE contrato_id = ?", (row1[8],)).fetchone

        for rw1 in cursor:
            print(rw1) 

        cursor.execute("SELECT * FROM dependencia WHERE dependencia_id = ?", (row1[9],)).fetchone

        for rw21 in cursor:
            print(rw21)

        cursor.execute("SELECT * FROM retroalimentacion WHERE mes = ?", (mes,)).fetchone

        for rw31 in cursor:
            print(rw31)
      
        return render_template('user_employee.html', nombre=row1[1], id=row1[0], direccion=row1[5], telefono=row1[6], inicio=rw1[1], contrato=row1[8], fin=rw1[2], dependencia=rw21[1], salario=rw1[3], feed=rw31[3])
              
    else:
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
    return render_template('add_employee.html', name=name)

@app.route('/admin/findemployee')
def adminFind():
    return render_template('find_employee.html')

@app.route('/admin/findemployee/find', methods = ('GET', 'POST'))
def find():

    if request.method=='POST':

        cedula = request.form['findbyname']
        
        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM empleado WHERE cedula = ?", (cedula,)).fetchone
        for row in cursor:
            print(row) 
        
        cursor.execute("SELECT * FROM contrato WHERE contrato_id = ?", (row[8],)).fetchone

        for rw in cursor:
            print(rw) 

        cursor.execute("SELECT * FROM dependencia WHERE dependencia_id = ?", (row[9],)).fetchone

        for rw2 in cursor:
            print(rw2)
      
        return render_template('find_employee.html', nombre=row[1], id=row[0], direccion=row[5], telefono=row[6], inicio=rw[1], contrato=row[8], fin=rw[2], dependencia=rw2[1], salario=rw[3])
        
        
    else: 

        return render_template('find_employee.html')

@app.route('/admin/Editemploye/')
def adminEdit():
    return render_template('edit_employee.html')

@app.route('/admin/Editemploye/findedit', methods=('GET', 'POST'))
def findEdit():

    if request.method=='POST':
        cedula = request.form['findbyname']
        
        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()
        
        cursor.execute("SELECT * FROM empleado WHERE cedula = ?", (cedula,)).fetchone
        for row in cursor:
            print(row) 
        
        cursor.execute("SELECT * FROM contrato WHERE contrato_id = ?", (row[8],)).fetchone

        for rw in cursor:
            print(rw) 

        cursor.execute("SELECT * FROM dependencia WHERE dependencia_id = ?", (row[9],)).fetchone

        for rw2 in cursor:
            print(rw2)
      
        return render_template('edit_employee.html', nombre=row[1], id=row[0], direccion=row[5], telefono=row[6], inicio=rw[1], contrato=row[8], fin=rw[2], dependencia=rw2[1], salario=rw[3])
        
    else:

        return render_template('edit_employee.html')
@app.route('/admin/Editemploye/edit', methods=('GET', 'POST'))
def Edit():

    if request.method=='POST':
        nombre = request.form['name']
        identificador=request.form['cedula']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        inicio = request.form['inicio']
        contrato = request.form['contract']
        fin = request.form['fin']
        salario = request.form['salario']
        mes=request.form['Mes']
        feedback=request.form['txtarea']

        con = sqlite3.connect('db_empleados.db')
        cursor = con.cursor()

        cursor.execute("UPDATE empleado SET nombre = ?, direccion = ?, telefono = ?  WHERE empleado_id = ?", (nombre, direccion, telefono, identificador))
        cursor.execute("UPDATE contrato SET fecha_inicio = ?, fecha_fin = ?, salario = ?  WHERE contrato_id = ?", (inicio, fin, salario, contrato))
        cursor.execute("INSERT INTO retroalimentacion (empleado_id, mes, feedback) values(?, ?, ?)", (identificador, mes, feedback))

        con.commit()
        con.close()

        return render_template('edit_employee.html', identificador=identificador)
    else:

        return render_template('edit_employee.html')

@app.route('/admin/deleteEmployee/')
@app.route('/superadmin/deleteEmployee/')
def adminDelete():
    return render_template('delete_employee.html')

@app.route('/superadmin/dashboard/')
def dashboard():
    return render_template('dashboard.html')

app.run(debug=True, host='127.0.0.1', port=5000)
