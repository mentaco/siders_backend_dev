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

@module_router.route('/follow_data', methods=['GET'])
def get_user_relation_router():
    user_id_from = request.args.get('user_id_from')
    user_id_to = request.args.get('user_id_to')
    return get_user_relation(user_id_from, user_id_to)

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
    arg1 = request.args.get('user_id')
    return get_notice_data(arg1)

@module_router.route('/get_student_id', methods=['GET'])
def get_student_id():
    email = request.args.get('mail_address')
    return get_student_id(email)

@module_router.route('/get_mypage_info', methods=['GET'])
def get_mypage_info():
    user_id = request.args.get('student_id')
    return get_mypage_info(user_id)

@module_router.route('/get_follow_info', methods=['GET'])
def get_follow_info():
    user_id = request.args.get('student_id')
    return get_follow_info(user_id)

@module_router.route('/get_follower_info')
def get_follower_info():
    user_id = request.args.get('student_id')
    return get_follower_info(user_id)

@module_router.route('/search_user_get', methods=['GET'])
def search_user_get_route():
    text = request.args.get('search_text')
    return search_user_get(text)
