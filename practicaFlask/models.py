from app import db
class Empleado(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre_empleado = db.Column(db.String(250))
    puesto = db.Column(db.String(250))
    
class Sucursal(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    descripcion=db.Column(db.String(255),nullable=False)
    nombre_sucursal=db.Column(db.String(255),nullable=False)

class Departamento(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre_departamento=db.Column(db.String(255),nullable=False)