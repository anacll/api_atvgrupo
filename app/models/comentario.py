from app import db
from datetime import datetime

class Comentario(db.Model):
    __tablename__ = "comentarios"

    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(500), nullable=False)
    dataHora = db.Column(db.DateTime, default=datetime.utcnow)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    mensagem_id = db.Column(db.Integer, db.ForeignKey('mensagens.id'), nullable=False)

    autor = db.relationship("Usuario", backref="comentarios")
    mensagem = db.relationship("Mensagem", backref="comentarios")
