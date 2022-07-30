"""
Routs for the api server
"""


import logging
from flask import Blueprint
from utils import consoleLog as log

apibp = Blueprint("apibp", __name__)

#! Main edpoint
@apibp.route('/')
def index():
    log.PipeLine_Ok("Ok UwU test endpoint~")

    return "<html><body></body></html>"

