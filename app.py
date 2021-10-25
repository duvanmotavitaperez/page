from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = os.urandom(4)
@app.route('/')
def login():
    print('Enviado')
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def user():
    if(request.method == 'POST'){
        user = request.form['user']
        print(user)
        return jsonify()
    }
@app.route('/app')
def response():
    return render_template('admin.html')
app.run(debug=True, port=5000, host='192.168.1.3')