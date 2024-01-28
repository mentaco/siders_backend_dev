from flask import Blueprint
from .modules import *

module_router = Blueprint('module_router', __name__)

@module_router.route('/example_data', methods=['GET'])
def example_get_data_route():
    return example_get_data()

@module_router.route('/example_data', methods=['POST'])
def example_add_data_route():
    return example_add_data()

@module_router.route('/example_data', methods=['DELETE'])
def example_del_data_route():
    return example_del_data()

@module_router.route('/follow_data', methods=['POST'])
def follow_request_add_route():
    return follow_request_add()

@module_router.route('/follow_data', methods=['DELETE'])
def user_relation_del_route():
    return user_relation_del()

