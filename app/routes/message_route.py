from flask import Blueprint
from ..controllers.message_controller import criar_mensagem
from ..controllers.message_controller import atualizar_mensagem

message_bp = Blueprint('mensagem', __name__)
@message_bp.route('/', methods=['POST'])
def route_post():
    return criar_mensagem()
@message_bp.route('/<int:id>', methods=['PUT'])
def route_put(id):
    return atualizar_mensagem(id)
