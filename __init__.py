from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@ app.route("/")
def home():
    return render_template('index.html')

@ app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
       user = request.form.get["name"]
       return redirect(url_for("user", usr = user))
    else :
       return render_template("login.html")
@ app.route("/<usr>")
def user(usr):
    return "<h1> Welcome {usr}</h1>"

if __name__ == "__main__":
    #app.debug = True
    #host = os.environ.get('IP','0.0.0.0')
    #port = int(os.environ.get('PORT',80))
    app.run(debug=True, host='localhost', port=8080)
