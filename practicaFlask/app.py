from flask import Flask
import logging
from flask_migrate import Migrate
from database import db
from config import BasicConfig
from routes.empleado.empleado import appEmpleado
from routes.sucursal.sucursal import appsucursal

app = Flask(__name__)

app.register_blueprint(appEmpleado)
app.register_blueprint(appsucursal)

app.config.from_object(BasicConfig)

db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG, filename = "debug.log")