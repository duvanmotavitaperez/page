from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os 

app = Flask(__name__)

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

        if username == "admin" and password == "admin123":
            
            return loginAdmin()

        elif username == "employee" and password == "employee123":

            return loginEmploye()

        elif username == "superadmin" and password == "superadmin123":
            
            return loginSuperadmin()

        else:
            return render_template('index.html')
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

@app.route('/admin/addemployee/')
def adminAdd():
    return render_template('add_employee.html')

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


