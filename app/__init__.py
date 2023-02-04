from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from .constants import *

from .models.entities.user import User

from .models.model_book import ModelBook
from .models.model_user import ModelUser

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


def not_found(error):
    return render_template('error_templates/404.html'), 404

def not_logged(error):
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user=User(None, request.form['username'], request.form['password'], None)
        user_logged = ModelUser.login(db, user)

        if user_logged != None:
            login_user(user_logged)
            flash(WELCOME_MESSAGE)
            return redirect(url_for('index'))
        else:
            flash(LOGIN_INVALID_CREDENTIALS, 'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT_SUCCEDED, 'success')
    return redirect(url_for('login'))


# Prueba de conexión a BD
@app.route('/books')
@login_required
def list_books():
    try:
        bks = ModelBook.listing_books(db)
        
        data = {
            'bks': bks
        }

        return render_template('trial_books.html', data=data)
    except Exception as e:
        raise Exception(e)



def app_init(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, not_logged)
    app.register_error_handler(404, not_found)
    return app