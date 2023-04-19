from flask import Flask
import logging
from flask_migrate import Migrate
from database import db
from config import BasicConfig
from routes.empleado.empleado import appEmpleado
from routes.sucursal.sucursal import appSucursal

app = Flask(__name__)

app.register_blueprint(appEmpleado)
app.register_blueprint(appSucursal)

app.config.from_object(BasicConfig)

db.init_app(app)
migrate = Migrate()
logging.basicConfig(level=logging.DEBUG, filename = "debug.log")
migrate.init_app(app,db)
