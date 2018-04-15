import os
from app import create_app
from flask_script import Manager, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
server = Server(host="159.89.150.55", port=9000)
manager = Manager(app)
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()
