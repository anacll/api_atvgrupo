from flask import Blueprint
from ..controllers.comentario_controller import criar_comentario, listar_comentarios_por_mensagem, atualizar_comentario, deletar_comentario

comentario_bp = Blueprint("comentario_bp", __name__)

@comentario_bp.route('/mensagens/<int:mensagem_id>/comentarios', methods=['POST'])
def route_post():
    return criar_comentario()

@comentario_bp.route("/mensagens/<int:mensagem_id>/comentarios", methods=['GET'])
def route_get():
    return listar_comentarios_por_mensagem()

@comentario_bp.route("/mensagens/<int:mensagem_id>/comentarios/<int:comentario_id>", methods=['PUT'])
def route_put():
    return atualizar_comentario()

@comentario_bp.route("/mensagens/<int:mensagem_id>/comentarios/<int:comentario_id>", methods=['DELETE'])
def route_delete():
    return deletar_comentario()