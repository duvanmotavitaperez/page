from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
app.run(host="192.168.1.7", port=5000)
@app.route("/<username>/<password>")
def user(username, password):
    return render_template("user.html", username, password)