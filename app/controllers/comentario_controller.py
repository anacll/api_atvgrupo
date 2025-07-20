from flask import request, jsonify
from app import db
from ..models.comentario import Comentario
from ..models.message import Mensagem

def buscar_comentario(mensagem_id, comentario_id):
    comentario = Comentario.query.get(comentario_id)
    if not comentario:
        return jsonify({"erro": "Comentário não encontrado"}), 404

    if comentario.mensagem_id != mensagem_id:
        return jsonify({"erro": "Comentário não pertence à mensagem informada"}), 400

    return jsonify({
        "id": comentario.id,
        "conteudo": comentario.conteudo,
        "dataHora": comentario.dataHora.isoformat(),
        "autorId": comentario.autor_id
    }), 200


def criar_comentario(mensagem_id):
    data = request.get_json()
    conteudo = data.get('conteudo')
    autor_id = 1  

    if not conteudo or conteudo.strip() == "":
        return jsonify({"erro": "Conteúdo não pode ser vazio"}), 400

    mensagem = Mensagem.query.get(mensagem_id)
    if not mensagem:
        return jsonify({"erro": "Mensagem não encontrada"}), 404

    novo_comentario = Comentario(conteudo=conteudo, autor_id=autor_id, mensagem_id=mensagem_id)
    db.session.add(novo_comentario)
    db.session.commit()

    return jsonify({"id": novo_comentario.id, "msg": "Comentário criado"}), 201


def listar_comentarios_por_mensagem(mensagem_id):
    comentarios = Comentario.query.filter_by(mensagem_id=mensagem_id).all()
    resultado = []
    for comentario in comentarios:
        resultado.append({
            "id": comentario.id,
            "conteudo": comentario.conteudo,
            "dataHora": comentario.dataHora.isoformat(),
            "autorId": comentario.autor_id
        })
    return jsonify(resultado), 200


def atualizar_comentario(mensagem_id, comentario_id):
    comentario = Comentario.query.get(comentario_id)
    if not comentario:
        return jsonify({"erro": "Comentário não encontrado"}), 404

    if comentario.mensagem_id != mensagem_id:
        return jsonify({"erro": "Comentário não pertence à mensagem informada"}), 400

    if comentario.autor_id != 2:  
        return jsonify({"erro": "Você não tem permissão para editar este comentário"}), 403

    data = request.get_json()
    novo_conteudo = data.get("conteudo")

    if not novo_conteudo or novo_conteudo.strip() == "":
        return jsonify({"erro": "Conteúdo não pode ser vazio"}), 400

    comentario.conteudo = novo_conteudo
    db.session.commit()
    return jsonify({"msg": "Comentário atualizado com sucesso"}), 200


def deletar_comentario(mensagem_id, comentario_id):
    comentario = Comentario.query.get(comentario_id)
    if not comentario:
        return jsonify({"erro": "Comentário não encontrado"}), 404

    if comentario.mensagem_id != mensagem_id:
        return jsonify({"erro": "Comentário não pertence à mensagem informada"}), 400

    if comentario.autor_id != 1:  # simulação de autenticação
        return jsonify({"erro": "Você não tem permissão para deletar este comentário"}), 403

    db.session.delete(comentario)
    db.session.commit()
    return jsonify({"msg": "Comentário deletado com sucesso"}), 200
