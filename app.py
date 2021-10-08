from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os 

app = Flask(__name__)
location = app.config['UPLOAD_FOLDER'] = 'files'

@app.route("/")
def login():
    return render_template("index.html")
    
app.run(debug=True, host='127.0.0.1', port=5000)