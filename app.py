from flask import Flask,request,jsonify
from main import PyJson, id_in_dict


app = Flask(__name__)
pyjson = PyJson("utf-8")
livros = pyjson.readjson("models/base.json")

@app.route("/",methods=["GET"])
def home():
    return jsonify(livros)


@app.route("/livros",methods=["GET"])
def quantidade_livros():
    return f"{len(livros)} Livros cadastrados"



    

if __name__ == '__main__':
   app.run(debug=True)

