from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from .constants import *
from .models.entities.user import User
from .models.entities.book import Book
from .models.entities.sale import Sale

from .models.model_book import ModelBook
from .models.model_user import ModelUser
from .models.model_sale import ModelSale

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


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


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.idUserAccess.idUserAccess == 1:
            try:    
                sold_items = ModelBook.list_sold_books(db)
                data = {
                    'title': 'Sold Items',
                    'sold_items': sold_items
                }
                return render_template('index.html', data=data)
            except Exception as e:
                return render_template('error_templates/error.html', message=format(e))
        else:
            try:
                my_books = ModelSale.list_user_items(db, current_user)
                data = {
                    'title': 'My Books',
                    'my_books': my_books
                }
                return render_template('index.html', data=data)
            except Exception as e:
                return render_template('error_templates/error.html', message=format(e))
    else:
        redirect(url_for('login'))



# Prueba de conexi??n a BD
@app.route('/books')
@login_required
def list_books():
    try:
        bks = ModelBook.listing_books(db)
        
        data = {
            'title': 'Book List',
            'bks': bks
        }

        return render_template('books.html', data=data)
    except Exception as e:
        return render_template('error_templates/error.html', message=format(e))


@app.route('/buybook', methods=['POST'])
@login_required
def buy_book():
    data_request = request.get_json()
    data={}

    try:
        book = Book(data_request['isbn'], None, None, None)
        user_purchase = Sale(None, book.isbn, current_user.idUser, None)
        print(vars(user_purchase))
        data['success'] = ModelSale.register(db, user_purchase)
    except Exception as e:
        data['message'] = format(e)
        data['mostrar'] = 'yo digo que aqui esta el error'
        data['success'] = False

    return jsonify(data)


def app_init(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, not_logged)
    app.register_error_handler(404, not_found)
    return app