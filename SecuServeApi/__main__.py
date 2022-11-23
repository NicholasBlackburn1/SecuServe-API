"""
main api server

"""


import pathlib
from app import create_app
from utils import logger,consts


def main():
    
    logger.info("cert paths"+ str(pathlib.Path().absolute())+"/data/"+'server.crt')

  

    app = create_app()

    app.run(threaded=True, debug=True, host=consts.url, port=2000)

# this sarts the file
if __name__ == "__main__":
    main()
