from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
with app.app_context():
    db.create_all()  

from .routes.user_route import user_bp
from .routes.message_route import message_bp
from .routes.comentario_route import comentario_bp

app.register_blueprint(user_bp, url_prefix='/usuarios')
app.register_blueprint(message_bp, url_prefix='/mensagens')
app.register_blueprint(comentario_bp)

print("Blueprint comentário registrado:", comentario_bp)


if __name__ == '__main__':
    app.run(debug=True)
