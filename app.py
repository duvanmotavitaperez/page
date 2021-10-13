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

@app.route('/login')
def login():
    return None

@app.route('/admin/addemployee/')
def adminAdd():
    return render_template('add_employee.html')

@app.route('/superadmin/dashboard/')
def dashboard():
    return render_template('dashboard.html')
app.run(debug=True, host='192.168.1.8', port=5000)

