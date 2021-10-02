from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    username = request.form.get("username")
    return render_template("index.html", username = username)
app.run(host="192.168.1.7", port=5000)