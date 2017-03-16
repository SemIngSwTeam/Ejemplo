CREATE TABLE usuario(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nombre TEXT, 
apellido1 TEXT,
apellido2 TEXT, 
correo TEXT, 
password TEXT, 
tipo INTEGER 
);
CREATE TABLE invernadero(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT,
ubicacion TEXT );
CREATE TABLE UsuarioInvernadero(
id_usuario INTEGER,
id_invernadero INTEGER, 
FOREIGN KEY (id_usuario) REFERENCES usuario(id),
FOREIGN KEY (id_invernadero) REFERENCES invernadero(id)
);
CREATE TABLE planta(
id INTEGER PRIMARY KEY AUTOINCREMENT,
cultivo TEXT, 
fecha DATE, 
id_invernadero REFERENCES invernadero(id)
);
CREATE TABLE registo(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fecha DATE, 
co_2 REAL, 
humedad REAL, 
temperatura REAL,
pH REAL, 
luz REAL, 
id_planta REFERENCES planta(id)
);
