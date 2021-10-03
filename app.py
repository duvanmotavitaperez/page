from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/angeles/")
def userAdd():
    user = request.args.get("username")
    password = request.args.get("password")
    return render_template("user.html", username = user ,password = password)
app.run(debug=True)