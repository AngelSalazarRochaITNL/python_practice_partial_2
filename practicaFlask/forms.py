from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EmpleadoForm(FlaskForm):
    nombre_empleado = StringField('Nombre', validators=[DataRequired()])
    puesto = StringField('Puesto', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class SucursalForm(FlaskForm):
    nombre_sucursal = StringField('Nombre', validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
