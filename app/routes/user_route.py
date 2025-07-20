from flask import Blueprint
from ..controllers.user_controller import criar_usuario
from ..controllers.user_controller import listar_usuarios
from ..controllers.user_controller import atualizar_usuario
from ..controllers.user_controller import deletar_usuario

user_bp = Blueprint('usuario', __name__)
@user_bp.route('/', methods=['POST'])
def route_post():
    return criar_usuario()
@user_bp.route('/', methods=['GET'])
def route_get():
    return listar_usuarios()
@user_bp.route('/<id>', methods=['PUT'])
def route_put(id):
    return atualizar_usuario(id)
@user_bp.route('/<id>', methods=['DELETE'])
def route_delete(id):
    return deletar_usuario(id)