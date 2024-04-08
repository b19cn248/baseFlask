from flask import Flask
from models import db  # Import db from models/__init__.py
from controller.book_controller import book_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/facebook'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Đăng ký ứng dụng với đối tượng SQLAlchemy
db.init_app(app)

with app.app_context():
    db.create_all()

# Đăng ký blueprint
app.register_blueprint(book_blueprint)

if __name__ == '__main__':
    app.run()
