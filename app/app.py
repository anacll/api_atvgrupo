from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.comentario import Comentario

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from models.user import Usuario
from models.message import Mensagem
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()  

from routes.user_route import user_bp
from routes.message_route import message_bp
from routes.comentario_route import comentario_bp

app.register_blueprint(comentario_bp)
app.register_blueprint(user_bp)
app.register_blueprint(message_bp)

if __name__ == '__main__':
    app.run(debug=True)
