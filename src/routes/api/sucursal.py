from flask import Blueprint, request, jsonify
import src.controllers.sucursal


sucursal_api_router = Blueprint('sucursal_api_router', __name__)
keys = ['name','city','country','address','description','phone']


@sucursal_api_router.route('/')
def get() :#{
    return src.controllers.sucursal.get()
#}

@sucursal_api_router.route('/<id>')
def get_id(id) :#{
    return src.controllers.sucursal.get_id(id)
#}

@sucursal_api_router.route('/', methods = ['POST'])
def post() :#{
    body : dict = { k : request.get_json().get(k) for k in keys } # body = { k : v for k, v in request.get_json().items() if k in keys}
    return src.controllers.sucursal.post(**body)
#}

@sucursal_api_router.route('/<id>', methods = ['PUT'])
def put(id) :#{
    body : dict = { k : request.get_json().get(k) for k in keys }
    return src.controllers.sucursal.put(id, **body)
#}

@sucursal_api_router.route('/<id>', methods = ['DELETE'])
def delete(id) :#{
    return src.controllers.sucursal.delete(id)
#}

# @sucursal_api_router.route('/get/<id>/')
@sucursal_api_router.route('/get/by/ubicacion/<country>')
@sucursal_api_router.route('/get/by/ubicacion/<country>/<city>')
def get_by_ubicacion(country, city = "") :#{
    return src.controllers.sucursal.get_by_ubicacion(country, city)
#}