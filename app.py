from flask import Flask, render_template,request,redirect,url_for
from main import PyJson 


app = Flask(__name__)
pyjson = PyJson("utf-8")
livros = pyjson.readjson("models/base.json")

@app.route("/",methods=["GET"])
def home():
    return livros
   # return render_template("index.html")


@app.route("/cadastrar",methods=["POST","GET"])
def cadastrar():
    
    if request.method == "GET":
        return render_template("cadastro.html")
    
    if request.method == "POST":
        nomde_de_livro = request.form['nomdeDoLivro']
        qtd_paginas = request.form['quntiadeDePginas']
        
        return redirect(url_for("redi"))
 

@app.route("/redi")
def redi():
    return "Estou na pagina de redirect"
    

if __name__ == '__main__':
   app.run(debug=True)

