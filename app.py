from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)  # Fixed app creation
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":  # Fixed from request.methods
        username = request.form.get("username")  # Changed == to =
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again.", mimetype="text/plain")  # Fixed typo

    return '''
        <h2>Login Page</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>  <!-- Changed to password -->
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href="{url_for("logout")}">Logout</a>  <!-- Fixed href and closing tag -->
        '''
    return redirect(url_for("login"))  # Fixed syntax

@app.route("/logout")
def logout():
    session.pop("user", None)  # Fixed None case
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
