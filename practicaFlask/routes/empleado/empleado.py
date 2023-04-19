from flask import Blueprint, request, jsonify,render_template,url_for,redirect
from models import Empleado
from forms import EmpleadoForm
from app import db

## los blueprints ayudan a construir sub aplicaciones, como sub proyectos, se hace independiente
## lo unico que cambia seria la db y el modelo
appEmpleado = Blueprint('appEmpleado',__name__,template_folder="templates")



## empleados
@appEmpleado.route('/')
@appEmpleado.route('/index')
def inicio():
    empleados = Empleado.query.all()
    totalDeempleados = Empleado.query.count()
    ##app.logger.debug(f'Listado de empleados {empleados}')
    return render_template('index.html', empleados = empleados, totalDeempleados = totalDeempleados)

    

@appEmpleado.route('/agregar', methods = ["GET","POST"])
def agregar(): 
    empleado = Empleado()
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method == "POST":
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            db.session.add(empleado)
            db.session.commit()
            return redirect(url_for('appEmpleado.inicio'))
    return render_template('agregar.html', forma = empleadoForm)

@appEmpleado.route('/editar/<int:id>',methods= ["GET","POST"])
def editar(id):
    empleado = Empleado.query.get_or_404(id)
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method == "POST":
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            db.session.commit()
            return redirect(url_for('appEmpleado.inicio'))
    return render_template('editar.html',forma=empleadoForm)

@appEmpleado.route('/eliminar/<int:id>')
def eliminar(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('appEmpleado.inicio'))