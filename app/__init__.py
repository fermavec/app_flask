from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from .models.model_book import ModelBook

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


def not_found(error):
    return render_template('error_templates/404.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    print(request.method)
    print(request.form('username'))
    print(request.form('password'))
    """
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '12345':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


# Prueba de conexión a BD
@app.route('/books')
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
    app.register_error_handler(404, not_found)
    return app