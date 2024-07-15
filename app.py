from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user
from db_engine import init_db
from models import User

app = Flask(__name__)
db = init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
