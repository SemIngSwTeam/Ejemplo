from flask import Flask, jsonify
from invernadero import administrador

app = Flask('inicio')
admin = administrador()


@app.route("/")
def index():
	return "Esta es la pagina raíz, se tiene la base de datos del invernadero. \
	Se tiene acceso a diferentes rutas las cuales son las siguientes: \
	 /usuarios  /invernaderos  /plantas  /registros"

@app.route("/usuarios")
def usuarios():
	datos = admin.mostrar_usuarios()
	datos = jsonify(datos)
	return datos

@app.route("/invernaderos")
def invernaderos():
	datos = admin.mostrar_invernaderos()
	datos = jsonify(datos)
	return datos

@app.route("/plantas")
def plantas():
	datos = admin.mostrar_plantas()
	datos = jsonify(datos)
	return datos

@app.route("/registros")
def registros():
	datos = admin.mostrar_registros()
	datos = jsonify(datos)
	return datos

app.run()
