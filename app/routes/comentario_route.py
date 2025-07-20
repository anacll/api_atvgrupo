from flask import Blueprint
from controllers import comentario_controller

comentario_bp = Blueprint("comentario_bp", __name__)

comentario_bp.post("/comentarios")(comentario_controller.criar_comentario)
comentario_bp.get("/mensagens/<int:mensagem_id>/comentarios")(comentario_controller.listar_comentarios_por_mensagem)
comentario_bp.put("/comentarios/<int:comentario_id>")(comentario_controller.atualizar_comentario)
comentario_bp.delete("/comentarios/<int:comentario_id>")(comentario_controller.deletar_comentario)
