import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt= Bcrypt()
loginmanager = LoginManager()



#application factory
def create_app(config_type): #dev, test or prod
    app = Flask(__name__, static_url_path='/static')
    configuration = os.path.join(os.getcwd(),'config' , config_type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bcrypt.init_app(app)
    loginmanager.init_app(app)

   #import blueprint
    from app.auth import auth
    app.register_blueprint(auth)



    return app




