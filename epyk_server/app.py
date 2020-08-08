from flask import Flask
from epyk_server.endpoints import welcome
app = Flask()



def init_app():
    global app
    app.register_blueprint(welcome)