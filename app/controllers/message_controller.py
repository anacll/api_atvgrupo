from flask import request, jsonify
from ..models.message import Mensagem
from app import db

def criar_mensagem():
    data = request.json
    nova_msg = Mensagem(conteudo=data['conteudo'], autor_id=1)  # autor padrão
    db.session.add(nova_msg)
    db.session.commit()
    return jsonify({'id': nova_msg.id}), 201

def atualizar_mensagem(id):
    msg = Mensagem.query.get_or_404(id)
    data = request.json

    if 'autor_id' in data and data['autor_id'] != msg.autor_id:
        return jsonify({'erro': 'Autor não pode ser alterado'}), 400

    msg.conteudo = data.get('conteudo', msg.conteudo)
    db.session.commit()
    return jsonify({'mensagem': 'Mensagem atualizada'})

