from flask import Flask, render_template
from waitress import serve
from version import last_version
from stability import stability_version

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ваш токен'

@app.route("/")
@app.route("/home")
def main():
    return render_template("main.html")

@app.route("/versions")
def lastversion():
    return render_template("versions.html", last_version=last_version, stability_version=stability_version)

@app.route("/ide")
def ide():
    return render_template("ide.html")

@app.route("/git")
def git():
    return render_template("git.html")

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=8080)
    print("http://127.0.0.1:8080")
    app.run(debug=True)