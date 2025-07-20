from datetime import datetime
from app import db

class Mensagem(db.Model):
    __tablename__ = 'mensagens'  

    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Text, nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    autor = db.relationship("Usuario", backref="mensagens")
