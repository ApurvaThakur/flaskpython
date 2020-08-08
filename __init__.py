from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

def login():
    if request.method == "POST":
	username = request.form["name"]
	return redirect(url_for("user", user=username))
    else:
	return render_template("login.html")
def user(usr):
    return f"<h1>Welcome {usr}</h1>"