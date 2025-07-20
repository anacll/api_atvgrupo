from flask import request, jsonify
from ..models.user import Usuario
from app import db


def criar_usuario():
    data = request.json
    try:
        usuario = Usuario(**data)
        db.session.add(usuario)
        db.session.commit()
        return jsonify({'id': usuario.id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.id, 'email': u.email, 'nome': u.nome} for u in usuarios])

def atualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.json
    try:
        usuario.nome = data.get('nome', usuario.nome)
        usuario.email = data.get('email', usuario.email)
        if 'senha' in data:
            usuario.senha = data['senha']
        db.session.commit()
        return jsonify({'mensagem': 'Usuário atualizado'})
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

def deletar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário deletado'})
