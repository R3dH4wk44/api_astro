from flask import Flask, Blueprint, jsonify, request
from Services.UserService import UserService
from validations.uservalidation import uservalidation
from flasgger import swag_from
import os
user = Blueprint('user',__name__, url_prefix='/user')

user_service = UserService()

@user.post('/login')
@swag_from('../documentation/user_documentation.json')
def login():
    
    try:
        user_name = request.json['user_name']
        password = request.json['password']
    except:
        return jsonify({"message": 'Username and password are Mandatorys'}), 400

    validation = uservalidation(user_name,password)

    if user_name is None:
        return jsonify({"message": 'Username is Mandatory'}), 400

    if password is None:
        return jsonify({"message": 'Password is Mandatory'}), 400

    user = user_service.login({"user_name":user_name, "password":password})
    
    if user['ok'] is False:
        return jsonify({"message":'User not Found'}), 404
    if user['ok'] is True and user['logged'] is False:
        return jsonify({"message":'Incorrect Password'}), 400

    return jsonify(user), 200


@user.post('/register')
def post_user():
    try:
        user_name = request.json['user_name']
        password = request.json['password']
    except:
        return jsonify({"message": 'Username and password are Mandatorys'}), 400

    validation = uservalidation(user_name,password)
    if validation['user_check'] == False or validation['password_check'] == False:
        return jsonify({"message": validation['error']}), 401

    user = user_service.register({"user_name":user_name,"password":password})

    if user['ok'] is False:
        return jsonify({"message": 'User already Exists'}), 409

    return jsonify({"username": user_name, "password": password}), 200
    
