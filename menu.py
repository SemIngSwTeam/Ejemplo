#ACTIVIDAD 03 - Rodríguez Seáñez José Miguel  - Seminario de solución de problemas de Base de Datos
from invernadero import administrador
class menu():
	admin = administrador()
	def __init__(self):
		while True:
			print("1) Agregar Usuario")
			print("2) Mostrar Usuarios")
			print("3) Agregar Invernadero")
			print("4) Mostrar Invernaderos")
			print("5) Agregar Planta")
			print("6) Mostrar Plantas")
			print("7) Insertar Registro")
			print("8) Mostrar Registros")
			print("0) Salir")
			op = input()

			if op == '1':
				#pedir datos
				lista = self.agregar_usuario()
				self.admin.insertar_usuario(lista)

			elif op == '2':
				#mostrar datos
				lista = self.admin.mostrar_usuarios()
				self.mostrar_usuarios(lista)
				#pass

			if op == '3':
				#pedir datos
				lista = self.agregar_invernadero()
				self.admin.insertar_invernadero(lista)

			elif op == '4':
				#mostrar datos
				lista = self.admin.mostrar_invernaderos()
				self.mostrar_invernaderos(lista)

			if op == '5':
				#pedir datos
				lista = self.agregar_planta()
				self.admin.insertar_planta(lista)

			elif op == '6':
				#mostrar datos
				lista = self.admin.mostrar_plantas()
				self.mostrar_plantas(lista)

			if op == '7':
				#pedir datos
				lista = self.agregar_registro()
				self.admin.insertar_registro(lista)

			elif op == '8':
				#mostrar datos
				lista = self.admin.mostrar_registros()
				self.mostrar_registros(lista)

			elif op == '0':
				exit()

	def agregar_usuario(self):
		nombre = input("Nombre")
		apellido1 = input("Apellido 1")
		apellido2 = input("Apellido 2")
		correo = input("Correo")
		password = input("Password")
		tipo = input("Tipo")

		return [nombre, apellido1, apellido2, correo, password, tipo]

	def mostrar_usuarios(self, lista):
		for e in lista:
			print(e)

	def agregar_invernadero(self):
		nombre = input("Nombre")
		ubicacion = input("Ubicacion")
		return [nombre, ubicacion]

	def mostrar_invernaderos(self, lista):
		for f in lista:
			print(f)

	def agregar_planta(self):
		cultivo = input("Cultivo")
		fecha = input("Fecha")
		id_invernadero = input("ID Invernadero")
		return [cultivo, fecha, id_invernadero]

	def mostrar_plantas(self, lista):
		for g in lista:
			print(g)

	def agregar_registro(self):
		fecha = input("Fecha")
		co_2 = input("Co2")
		humedad = input("Humedad")
		temperatura = input("Temperatura")
		pH = input("PH")
		luz = input("Luz")
		id_planta = input("ID Planta")

	def mostrar_registros(self, lista):
		for h in lista:
			print(h)

m = menu()
