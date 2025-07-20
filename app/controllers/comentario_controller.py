from flask import request, jsonify
from app import db
from ..models.comentario import Comentario
from ..models.message import Mensagem

def criar_comentario():
    data = request.get_json()

    conteudo = data.get('conteudo')
    mensagem_id = data.get('mensagemId')
    autor_id = 1  # padrão

    if not conteudo or conteudo.strip() == "":
        return jsonify({"erro": "O conteúdo não pode ser vazio"}), 400

    mensagem = Mensagem.query.get(mensagem_id)
    if not mensagem:
        return jsonify({"erro": "Mensagem não encontrada"}), 404

    novo = Comentario(
        conteudo=conteudo,
        mensagem_id=mensagem_id,
        autor_id=autor_id
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({"msg": "Comentário criado", "id": novo.id}), 201


def listar_comentarios_por_mensagem(mensagem_id):
    comentarios = Comentario.query.filter_by(mensagem_id=mensagem_id).all()
    resultado = [
        {
            "id": c.id,
            "conteudo": c.conteudo,
            "dataHora": c.dataHora.isoformat(),
            "autorId": c.autor_id
        } for c in comentarios
    ]
    return jsonify(resultado)


def atualizar_comentario(comentario_id):
    from models.comentario import Comentario
    comentario = Comentario.query.get(comentario_id)
    if not comentario:
        return jsonify({"erro": "Comentário não encontrado"}), 404

    data = request.get_json()
    if 'autor_id' in data or 'mensagem_id' in data:
        return jsonify({"erro": "Não é permitido alterar autor ou mensagem"}), 400

    if 'conteudo' in data:
        if data['conteudo'].strip() == "":
            return jsonify({"erro": "Conteúdo vazio"}), 400
        comentario.conteudo = data['conteudo']

    db.session.commit()
    return jsonify({"msg": "Comentário atualizado"})


def deletar_comentario(comentario_id):
    comentario = Comentario.query.get(comentario_id)
    if not comentario:
        return jsonify({"erro": "Comentário não encontrado"}), 404

    if comentario.autor_id != 1:
        return jsonify({"erro": "Você só pode excluir seus próprios comentários"}), 403

    db.session.delete(comentario)
    db.session.commit()
    return jsonify({"msg": "Comentário deletado com sucesso"})
