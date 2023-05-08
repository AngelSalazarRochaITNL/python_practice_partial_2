from models import Usuario
from flask import request, jsonify
from functools import wraps

def obtenerInfor(token):
    if token:
        resp=Usuario.decode_auth_token(token)
        user=Usuario.query.filter_by(id=resp).first()

        if user:
            infoUsuario = {
                'status': 'success',
                'data': {
                    'user_id':user.id,
                    'email':user.email,
                    'admi':user.admin,
                    'registrado': user.registrado
                }
            }
            return infoUsuario
        else:
            error={
                'status':'fail',
                'message':resp
            }
            return error
    
def tokenCheck(f):
    @wraps(f)
    def verificar(*args,**kwargs):
        token=None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return jsonify({'message':'token no encontrato'})
        try:
            info=obtenerInfor(token)
            if info['status'] == 'fail':
                return jsonify({'message':'token invalido'})
        except:
            return jsonify({'message':'token invalido'})
        return f(info['data'], *args, **kwargs)
    return verificar