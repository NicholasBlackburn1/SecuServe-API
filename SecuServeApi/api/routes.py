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
from utils import logger,filedownloader
import uuid


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
usr section of db
"""
@apibp.route(consts.user_data + "createuser", methods=["POST"])
def createUser():
    
    logger.warning("creating New User in the db...")
    logger.PipeLine_Ok("got User info successfully")

    #! user data
    user = app.UserData(**request.json)

    user.id = str(uuid.uuid4())
    user.name = request.json['name']
    user.group = request.json['group']
    user.phonenumber = request.json['phonenumber']

    #checks if user is in the db\
    if ( app.db.session.query(app.UserData).filter_by(id=user.id).scalar() is not None ):
       
        logger.Error("Entry exsits wont create a new one!")
        return jsonify({"status": "usr in db already", "users face": str(user.id)})
    
    logger.warning("saving user into to db...")


    app.db.session.add(user)
    app.db.session.commit()

    # saves the avis
    logger.PipeLine_Ok("saved user to db....")

    # logs the count of the avis in the db
    logger.PipeLine_Data(
        "entries in db is "
        + str(app.db.session.query(app.UserData).count())
    )
    
    
    return jsonify({"status": "sent users faces", "user": str(user.id)})




# gets all the Users from the db
@apibp.route(consts.user_data + "getallusers", methods=["GET"])

def getallusrs():
    logger.warning("got all the users data")

    logger.info("getting data....")

    users = app.UserData.query.filter_by().all()
    data = []
    logger.warning("Data Users" + str(users))
    # data sent in the lists is 0,1,2,3
    for i in range(int(app.db.session.query(app.UserData).count())):
        data.append(
            [
                users[i].id,
                users[i].name,
                users[i].group,
                users[i].phonenumber,
            ]
        )

    logger.PipeLine_Ok("got all users from db..")

    return jsonify(data)



# gets users face
@apibp.route(consts.user_data + "getUser", methods=["POST"])
def getalluserinfo():
    
    id = request.json["id"]
    
    logger.warning("gets user " + str(id) + "data.....")

    usr = app.UserData.query.filter_by(id=str(id)).all()
    data = []
    logger.warning("Data Users" + str(usr))
    # data sent in the lists is 0,1,2,3
    for i in range(int(app.db.session.query(app.UserData).filter_by(id=str(id)).count())):
        data.append(
            [
                usr[i].id,
                usr[i].name,
                usr[i].group,
                usr[i].phonenumber,
               
                
            ]
        )

    logger.PipeLine_Ok("got users face data uwu...")

    return jsonify(data)






"""
Face cration for facial rec
"""
@apibp.route(consts.face_data + "createface", methods=["POST"])

def createFace():

    logger.warning("creating New faces in the db...")

    logger.PipeLine_Ok("got faces info successfully")
    #! face data
    face = app.FaceData(**request.json)

    face.usr_id = request.json['usr_id']

    face.face_name = request.json['face_name']
    face.face2_name = request.json['face2_name']
    
    #! downloads the face data
    face.face_url = filedownloader.facedownloader(url=request.json['face_url'],face_name=request.json['face_name'])
    face.face2_url = filedownloader.facedownloader(url=request.json['face2_url'],face_name=request.json['face2_name'])
    
       

    if ( app.db.session.query(app.FaceData).filter_by(usr_id=face.usr_id).scalar() is not None ):
       
        logger.Error("Entry exsits wont create a new one!")
        return jsonify({"status": "face in db already", "users face": str(face.usr_id)})
       

    elif filedownloader.facedownloader(
        url=face.face_url,  face_name=face.face_name) != -2:

        logger.warning("saving face into to db...")


        app.db.session.add(face)
        app.db.session.commit()

        # saves the avis
        logger.PipeLine_Ok("saved face to db....")

        # logs the count of the avis in the db
        logger.PipeLine_Data(
            "entries in db is "
            + str(app.db.session.query(app.FaceData).count())
        )
        
       
        return jsonify({"status": "sent users faces", "user": str(face.usr_id)})



# gets all the faces from the db

@apibp.route(consts.face_data + "getallfaces", methods=["GET"])

def getallFaces():
    logger.warning("got all the users faces")

    logger.info("getting faces....")

    face = app.FaceData.query.filter_by().all()
    data = []
    logger.warning("Data faces" + str(face))
    # data sent in the lists is 0,1,2,3
    for i in range(int(app.db.session.query(app.FaceData).count())):
        data.append(
            [
                face[i].usr_id,
                face[i].face_name,
                face[i].face_url,
                face[i].face2_name,
                face[i].face2_url,
            ]
        )

    logger.PipeLine_Ok("got all faces from db..")

    return jsonify(data)


# gets users face
@apibp.route(consts.face_data + "getUsrsFace", methods=["POST"])
def getallaviduser():
    
    id = request.json["usr_id"]
    
    logger.warning("gets user " + str(id) + "data.....")

    face = app.FaceData.query.filter_by(usr_id=str(id)).all()
    data = []
    logger.warning("Data face" + str(face))
    # data sent in the lists is 0,1,2,3
    for i in range(int(app.db.session.query(app.FaceData).filter_by(usr_id=str(id)).count())):
        data.append(
            [
                face[i].usr_id,
                face[i].face_name,
                face[i].face_url,
                face[i].face2_name,
                face[i].face2_url,
                
            ]
        )

    logger.PipeLine_Ok("got users face data uwu...")

    return jsonify(data)


