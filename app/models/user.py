from sqlalchemy.orm import validates
import re
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # <- necessário para bater com os ForeignKeys

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(128), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("Email inválido")
        return email

    @validates('senha')
    def validate_password(self, key, senha):
        if (len(senha) < 8 or
            not re.search(r'[A-Z]', senha) or
            not re.search(r'[a-z]', senha) or
            not re.search(r'[0-9]', senha) or
            not re.search(r'[@!%*?&]', senha)):
            raise ValueError("Senha fraca")
        return senha
