from flask import Blueprint
from ..controllers.comentario_controller import (
    criar_comentario,
    listar_comentarios_por_mensagem,
    atualizar_comentario,
    deletar_comentario,
    buscar_comentario
)

comentario_bp = Blueprint("comentario_bp", __name__)

# Criar comentário
@comentario_bp.route('/mensagens/<int:mensagem_id>/comentarios', methods=['POST'])
def route_post(mensagem_id):
    return criar_comentario(mensagem_id)

# Listar comentários por mensagem
@comentario_bp.route("/mensagens/<int:mensagem_id>/comentarios", methods=['GET'])
def route_get(mensagem_id):
    return listar_comentarios_por_mensagem(mensagem_id)

@comentario_bp.route("/mensagens/<int:mensagem_id>/comentarios/<int:comentario_id>", methods=['GET'])
def route_get_comentario(mensagem_id, comentario_id):
    return buscar_comentario(mensagem_id, comentario_id)

# Atualizar comentário
@comentario_bp.route("/mensagens/<int:mensagem_id>/comentarios/<int:comentario_id>", methods=['PUT'])
def route_put(mensagem_id, comentario_id):
    return atualizar_comentario(mensagem_id, comentario_id)

# Deletar comentário
@comentario_bp.route("/mensagens/<int:mensagem_id>/comentarios/<int:comentario_id>", methods=['DELETE'])
def route_delete(mensagem_id, comentario_id):
    return deletar_comentario(mensagem_id, comentario_id)
