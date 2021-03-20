from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import loginManager, current_user
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'users.login'
login.login_message_category = 'info'

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()


from app.users.routes import users
from app.posts.routes import posts
from app.main.routes import users

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)


from app import models