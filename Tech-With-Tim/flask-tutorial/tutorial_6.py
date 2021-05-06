from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "201074"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Realizado com sucesso!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Você já está logado!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return redirect(url_for("user.html", user=user))
    else:
        flash("Você não está logado!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
        flash("Você está deslogado", "info")
        session.pop("user", None)
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)