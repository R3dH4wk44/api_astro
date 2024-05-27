from flask import Flask, Blueprint, request, jsonify
from Services.LaunchService import LaunchService


launch = Blueprint('launch', __name__, url_prefix='/launch')

launch_service = LaunchService()
@launch.get('/')
def get_all_launches():
    launches = launch_service.get_launch_list()
    
    if launches['ok'] is False:
        return launches['body'], 404
    return jsonify(launches['body']), 200



@launch.get('/<uuid:launch_id>')
def get_single_launch(launch_id):
    return '<Single Launch>', 200