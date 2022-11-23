"""
main api server rout
"""
import app
from utils import consts
from crypt import methods
from datetime import datetime
import json

from pyexpat import model
from urllib import response
from xmlrpc.client import DateTime
from charset_normalizer import logging
from flask import Blueprint, abort
from flask import (
    jsonify,
    render_template,
    redirect,
    request,
    url_for,
    send_from_directory,
    send_file,
)
import requests
from utils import logger



apibp = Blueprint("apibp", __name__)


"""
status section of my api
"""

# sends the api status
@apibp.route(consts.apibase + "status")
def status():
  
    logger.warning(
        "some one pulled the status of the api~ mabie they are smarties~ hope they wana help me ~"
    )
    return jsonify(
        '{"status":"online","information:"'
        + "OWO whats this my api is up OwO~ this api is made by foxgirl, if u see this please contact me at nickblackburn02@gmail.com to help me with my project~"
        + "}"
    )


"""
Face cration for facial rec
"""
@apibp.route(consts.database + "createuser", methods=["POST"])

def createFace():

    logger.warning("creating New faces in the db...")

    logger.PipeLine_Ok("got faces info successfully")
    #! face data
    face = app.FaceData(**request.json)

    face.usr_id = request.json['usr_id']

    face.face_name = request.json['face_name']
    face.face2_name = request.json['face_name']
    face.face_url = request.json['face_url']
    face.face2_url = request.json['face_url2']