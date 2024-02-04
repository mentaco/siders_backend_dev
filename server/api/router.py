from flask import Blueprint
from .modules import *

module_router = Blueprint('module_router', __name__)

@module_router.route('/example_data', methods=['GET'])
def example_get_data_route():
    arg1 = request.args.get('param1')
    arg2 = request.args.get('param2')

    return example_get_data(arg1, arg2)

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

@module_router.route('/get_message', methods=['GET'])
def get_message_route():
    arg1 = request.args.get('user_id')
    print(arg1)
    return get_message(arg1)

@module_router.route('/add_message', methods=['POST'])
def add_message_route():
    return add_message()

@module_router.route('/get_notice_data', methods=['GET'])
def get_notice_data_route():
    return get_notice_data()
