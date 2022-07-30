"""
Main app class
"""


from pathlib import Path
from utils import consoleLog as logger



# this cofigs the db
def configure_database(app, db):
    @app.before_first_request
    def initialize_database():
        logger.warning("Creating db... ")

        db.create_all()
        db.session.commit()

        logger.PipeLine_Ok("created db successfully.")

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


# this makes the local file paths for storing the data
def makePaths():

    if Path(str(Path().absolute()) + Consts.basepath).exists:
        # base bath
        logger.info("creating file structure for prgram...")

        Path(str(Path().absolute()) + Consts.basepath).mkdir(
            parents=True, exist_ok=True
        )

        # avi paths
        Path(str(Path().absolute()) + Consts.asset_all).mkdir(
            parents=True, exist_ok=True
        )
        Path(str(Path().absolute()) + Consts.asset_pc).mkdir(
            parents=True, exist_ok=True
        )
        Path(str(Path().absolute()) + Consts.asset_quest).mkdir(
            parents=True, exist_ok=True
        )
        Path(str(Path().absolute()) + Consts.aviimage).mkdir(
            parents=True, exist_ok=True
        )

        # user paths
        Path(str(Path().absolute()) + Consts.usrimg).mkdir(
            parents=True, exist_ok=True
        )


         # assetripper paths
        Path(str(Path().absolute()) + Consts.ripper).mkdir(
            parents=True, exist_ok=True
        )

        logger.PipeLine_Ok("created paths successfully")

    else:
        logger.warning("the paths exist cannot create them uwu~")



    
def create_app():

#! zero mq pub 
    logger.info("creating the folder patjhs...")
    makePaths()

    # checks for aries status
    if aries.getAriesStatus() == True:
        logger.info("Aries is UP UWU~")

    else:
        logger.Error("ARIES IS DOWN only using local db")

    # creates the flask app
    logger.Warning("Creating flask app...")
    app = Flask(__name__, static_url_path="/files", static_folder="FoxConnector-Data/static")

    logger.PipeLine_Ok("started flaskapp")

    logger.info("registered blueprints")






    app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "Fox_Connector",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "version": "1.0.0",
            "title": "FoxClient API",
            "endpoint": '/foxclient/api/docs',
            "description": 'This is the version 1 of our API',
            "route": '/foxclient/api/v1.0/',
        }
    ]
}

    Swagger(app)
   
    app.register_blueprint(example_blueprint)
    app.register_blueprint(routes.apibp)
    logger.PipeLine_Ok("REGISTERED blueprints")

    logger.info("setting foxserver database..")
    configure_database(app, db)
    db.init_app(app)
    DebugToolbarExtension(app)


   
    



    

    return app
