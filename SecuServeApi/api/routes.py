"""
Routs for the api server
"""


import logging
from flask import Blueprint, jsonify
from utils import consoleLog as log

# this section is for the urls of my api


version = "v1.0/"
apibase = "/secuserve/api/"+version

apibp = Blueprint("apibp", __name__)


"""
status of api 
"""
@apibp.route(apibase + "status")
def status():
  

    log.warning(
        "some one pulled the status of the api~ mabie they are smarties~ hope they wana help me ~"
    )
    return jsonify(
        '{"status":"online","information:"'
        + "OWO whats this my api is up OwO~ this api is made by foxgirl, if u see this please contact me at nickblackburn02@gmail.com to help me with my project~"
        + "}"
    )
