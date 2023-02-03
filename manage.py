from app import app_init
from config import config

from flask_script import Manager, Server

configuration = config['development']
app = app_init(configuration)

manager = Manager(app)
manager.add_command('runserver', Server(host='127.0.0.1', port=5005))


if __name__ == '__main__':
    manager.run()