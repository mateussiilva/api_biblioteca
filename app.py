from flask import Flask, render_template
from main import PyJson


app = Flask(__name__)
pyjson = PyJson("utf-8")
livros = pyjson.readjson("models/base.json")

@app.route("/")
def home():
    return render_template("home.html",livros=livros)



if __name__ == '__main__':
   app.run(debug=True)

