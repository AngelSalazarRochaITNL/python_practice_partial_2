from flask import Blueprint, request, jsonify,render_template,url_for,redirect
from models import Sucursal
from app import db


appsucursal = Blueprint('appsucursal',__name__,template_folder="templates")

## Sucursal ##
@appsucursal.route('/sucursal/agregar',methods=["POST"])
def agregarSucursal():
    try:
        json=request.get_json()
        sucursal = Sucursal()
        sucursal.nombre = json['nombre']
        sucursal.descripcion = json  ['descripcion']
        db.session.add(sucursal)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Sucursal agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appsucursal.route('/sucursal/editar',methods=["POST"])
def editarSucursal():
    try:
        json=request.get_json()
        pucursal=Sucursal.query.get_or_404(json["id"])
        pucursal.nombre = json["nombre"]
        pucursal.descripcion = json["descipcion"]
        db.session.commit()
        return jsonify({"status":"OK","mensaje":"Sucursal editada"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appsucursal.route('/sucursal/eliminar',methods=["POST"])
def eliminarSucursal():
    try:
        json=request.get_json()
        sucursal=Sucursal.query.get_or_404(json["id"])
        db.session.delete(sucursal)
        db.session.commit()
        return jsonify({"status":"OK","mensaje":"Sucursal eliminada"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appsucursal.route('/sucursal/obtener',methods=["GET"])
def obtenerSucursal():
    try:
        sucursales=Sucursal.query.all()
        listaSucursales=[]
        for p in sucursales:
            sucursal={}
            sucursal["nombre"]=p.nombre
            sucursal["descripcion"] = p.descripcion
            listaSucursales.append(sucursal)
        return jsonify({"status":"OK","mensaje":listaSucursales})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})