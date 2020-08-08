from flask import Flask
from epyk_server.endpoints import welcome


app = Flask(__name__)

def init_app():
    global app
    app.register_blueprint(welcome.welcome)
    return app

if __name__ == '__main__':
    my_app = init_app()
    my_app.run()
