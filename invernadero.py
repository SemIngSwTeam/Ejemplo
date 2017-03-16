#ACTIVIDAD 04 - Rodríguez Seáñez José Miguel  - Seminario de solución de problemas de Base de Datos
import sqlite3

class administrador():
	def __init__(self):
		self.db = sqlite3.connect("invernadero.db")
		self.c = self.db.cursor()

# TABLA 1 USUARIOS

	def mostrar_usuarios(self):
		t = self.c.execute("SELECT * FROM usuario")
		lista = []
		for e in t:
			d = {'ID': e[0], 'Nombre': e[1], 'Apellido1': e[2], 'Apellido2': e[3], 'Correo': e[4], \
			'Password': e[5], 'Tipo': e[6]}
			lista.append(d)
		return lista
	def insertar_usuario(self,lista):
		self.c.execute("INSERT INTO usuario (nombre, apellido1, apellido2, \
		correo, password, tipo) VALUES(?,?,?,?,?,?)", (lista[0], \
		lista[1], lista[2], lista[3], lista[4], lista[5]) )
		self.db.commit()

# TABLA 2 INVERNADEROS

	def mostrar_invernaderos(self):
		i = self.c.execute("SELECT * FROM invernadero")
		lista = []
		for f in i:
			q = {'ID': f[0], 'Nombre': f[1], 'Ubicacion':f[2]}
			lista.append(q)
		return lista
	def insertar_invernadero(self,lista):
		self.c.execute("INSERT INTO invernadero (nombre, ubicacion) VALUES (?,?)", (lista[0], \
		lista[1]))
		self.db.commit()


# TABLA 3 PLANTAS

	def mostrar_plantas(self):
		j = self.c.execute("SELECT * FROM planta")
		lista = []
		for g in j:
			w = {'ID': g[0], 'Cultivo': g[1], 'Fecha': g[2], 'Id Invernadero':g[3]}
			lista.append(w)
		return lista

	def insertar_planta(self,lista):
		self.c.execute("INSERT INTO planta (cultivo, fecha, id_invernadero) VALUES (?,?,?)", (lista[0],\
		lista[1], lista[2]))
		self.db.commit()


# TABLA 4 REGISTRO

	def mostrar_registros(self):
		k = self.c.execute("SELECT * FROM registo")
		lista = []
		for h in k:
			d = {'ID': h[0], 'Fecha': h[1], 'Dioxido de carbono': h[2], 'Humedad': h[3], 'Temperatura': h[4], \
			'pH': h[5], 'Luz': h[6], 'ID Planta': h[7]}
			lista.append(d)
		return lista

	def insertar_registro(self,lista):
		self.c.execute("INSERT INTO registo (fecha, co_2, humedad, temperatura, pH, luz, id_planta) VALUES (?,?,?,?,?,?,?)", \
		(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6]))
		self.db.commit()
