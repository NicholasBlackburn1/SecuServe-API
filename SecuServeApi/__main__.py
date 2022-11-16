"""
main api server

"""


import pathlib
from app import create_app
from utils import logger,consts



#
def main():


    logger.info("starting api server UWu~....")

    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + str(pathlib.Path().absolute()) + consts.basepath + "data.db"
    )

    
    

    app.run(threaded=True, debug=True, host=consts.url, port=2000)





if __name__ == '__main__':
    main()