
from pathlib import Path
import pathlib
from charset_normalizer import api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils import consts  # new

from importlib import import_module
from utils import logger
from api import routes


db = SQLAlchemy()

# data for the users in the face rec
class UserData(db.Model):
    __tablebname__="UserData"
    __table_args__ = {"sqlite_autoincrement": True}

    id = db.Column(db.String(255), primary_key=True)
    name= db.Column(db.String(255))
    group = db.Column(db.String(255))
    phonenumber = db.Column(db.String(255))

# face info
class FaceData(db.Model):
    __tablebname__="FaceData"
    __table_args__ = {"sqlite_autoincrement": True}

    usr_id = db.Column(db.String(255), primary_key=True)

    face_name = db.Column(db.String(255))
    face_url = db.Column(db.String(255))

    face2_name = db.Column(db.String(255))
    face2_url = db.Column(db.String(255))


# this cofigs the db
def configure_database(app, db):
    @app.before_first_request
    def initialize_database():
        logger.warning("Crealatform: str, aviName: strting db... ")

        db.create_all()
        db.session.commit()

        logger.PipeLine_Ok("created db successfully.")

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


# this makes the local file paths for storing the data
def makePaths():

    if Path(str(Path().absolute()) + consts.basepath).exists:
        # base bath
        logger.info("creating file structure for prgram...")

        Path(str(Path().absolute()) + consts.basepath).mkdir(
            parents=True, exist_ok=True
        )

        # avi paths
        Path(str(Path().absolute()) + consts.faces).mkdir(
            parents=True, exist_ok=True
        )

        # avi paths
        Path(str(Path().absolute()) + consts.static).mkdir(
            parents=True, exist_ok=True
        )

        logger.PipeLine_Ok("created paths successfully")

    else:
        logger.warning("the paths exist cannot create them uwu~")


def create_app():

    #! zero mq pub
    logger.info("creating the folder patjhs...")
    makePaths()

   
    logger.Warning("Creating flask app...")
    app = Flask(__name__, static_url_path="/files",
                static_folder=consts.basepath+"/static")

    app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' + str(pathlib.Path().absolute()) + consts.basepath + 'data.db')

    

    logger.PipeLine_Ok("started flaskapp")

    logger.info("registered blueprints")
    app.register_blueprint(routes.apibp)
    logger.PipeLine_Ok("REGISTERED blueprints")

    logger.info("setting  database..")
    configure_database(app, db)
    db.init_app(app)

    return app







    



