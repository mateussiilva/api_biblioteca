from flask import Flask,jsonify, render_template
from main import PyJson 


app = Flask(__name__)
pyjson = PyJson("utf-8")
livros = pyjson.readjson("models/base.json")

@app.route("/",methods=["GET"])
def home():
    # return jsonify(livros)
    return livros


@app.route("/livros",methods=["GET"])
def quantidade_livros():
    titulos = tuple(map(lambda id: livros[id]["titulo"],livros))
    return f"{titulos}"



    

if __name__ == '__main__':
   app.run(debug=True)

