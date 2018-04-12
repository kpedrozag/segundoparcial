from flask import Flask, render_template, jsonify
import primos_num as p
import sqlite3


app = Flask(__name__)


@app.route("/")
def nombre_en_pantalla():
    return render_template('nombre.html')


@app.route("/prime/<int:entero>")
def primo(entero):
    ls = p.principal(entero)
    return render_template('prime.html', lista=ls, num=entero)


@app.route("/prime/<int:e>/json")
def primo_json(e):
    ls = p.principal(e)

    return jsonify(info="Numeros primos desde el 0 hasta "+str(e),
                   valores=ls,
                   autor="KEVIN ANDRES PEDROZA GOENAGA")