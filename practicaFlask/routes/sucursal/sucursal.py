from flask import Blueprint, request, jsonify,render_template,url_for,redirect
from models import Sucursal
from forms import SucursalForm
from app import db

appSucursal = Blueprint('appSucursal',__name__,template_folder="templates")

## Sucursales
@appSucursal.route('/indexs')
def inicioSucursal():
    sucursales = Sucursal.query.all()
    totalDesucursales = Sucursal.query.count()
    return render_template('indexS.html', sucursales = sucursales, totalDeSucursales = totalDesucursales)

    
@appSucursal.route('/agregarS', methods = ["GET","POST"])
def agregarS(): 
    sucursal = Sucursal()
    sucursalForm = SucursalForm(obj=sucursal)
    if request.method == "POST":
        if sucursalForm.validate_on_submit():
            sucursalForm.populate_obj(sucursal)
            db.session.add(sucursal)
            db.session.commit()
            return redirect(url_for('appSucursal.inicioSucursal'))
    return render_template('agregarS.html', forma = sucursalForm)

@appSucursal.route('/editarS/<int:id>',methods= ["GET","POST"])
def editarSucursal(id):
    sucursal = Sucursal.query.get_or_404(id)
    sucursalForm = SucursalForm(obj=sucursal)
    if request.method == "POST":
        if sucursalForm.validate_on_submit():
            sucursalForm.populate_obj(sucursal)
            db.session.commit()
            return redirect(url_for('appSucursal.inicioSucursal'))
    return render_template('editarS.html',forma=sucursalForm)

@appSucursal.route('/eliminarS/<int:id>')
def eliminarS(id):
    sucursal = Sucursal.query.get_or_404(id)
    db.session.delete(sucursal)
    db.session.commit()
    return redirect(url_for('appSucursal.inicioSucursal'))