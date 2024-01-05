from flask import Flask,request
from main import PyJson


app = Flask(__name__)
pyjson = PyJson("utf-8")
livros = pyjson.readjson("models/base.json")

@app.route("/",methods=["GET"])
def home():
    return livros

@app.route("/livros",methods=["GET"])
def quantidade_livros():
    return f"{len(livros)} Livros cadastrados"

@app.route("/<int:id>", methods=["GET","POST"])
def buscar_livro(id: int):
    ids_livros = len(livros)
    if id > 0 and id <= ids_livros:
        return livros.get(str(id))
    else:
        return f"[ERRO] o ID '{id}' não existe no banco de dados".upper()
    
@app.route("/cadastrar/")
def cadastrar_livro():
    return request.args.to_dict
    
    

if __name__ == '__main__':
   app.run(debug=True)

