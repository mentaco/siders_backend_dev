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
def get_student_id_route():
    email = request.args.get('mail_address')
    return get_student_id(email)

@module_router.route('/get_mypage_info', methods=['GET'])
def get_mypage_info_route():
    user_id = request.args.get('student_id')
    return get_mypage_info(user_id)

@module_router.route('/get_follow_info', methods=['GET'])
def get_follow_info_route():
    user_id = request.args.get('student_id')
    return get_follow_info(user_id)

@module_router.route('/get_follower_info', methods=['GET'])
def get_follower_info_route():
    user_id = request.args.get('student_id')
    return get_follower_info(user_id)

@module_router.route('/skill_info', methods=['GET'])
def get_skill_info_route():
    user_id = request.args.get('student_id')
    return get_skill_info(user_id)

@module_router.route('/skill_info', methods=['POST'])
def add_skill_info_route():
    return add_skill_info()

@module_router.route('/skill_info', methods=['DELETE'])
def del_skill_info_route():
    return del_skill_info()

@module_router.route('/skill_info', methods=['PUT'])
def update_skill_info_route():
    return update_skill_info()

@module_router.route('/get_followed_new_posts', methods=['GET'])
def get_followed_users_post_new_route():
    students_list = request.args.get('students_list')
    focus_time = request.args.get('focus_time')
    return get_followed_users_post_new(students_list,focus_time)

@module_router.route('/get_followed_old_posts', methods=['GET'])
def get_followed_users_post_old_route():
    students_list = request.args.get('students_list')
    focus_time = request.args.get('focus_time')
    return get_followed_users_post_old(students_list,focus_time)

@module_router.route('/get_follow_list', methods=['GET'])
def get_follow_list_route():
    student_id = request.args.get('student_id')
    return get_follow_list(student_id)

@module_router.route('/get_my_interests', methods=['GET'])
def get_my_interests_route():
    student_id = request.args.get('student_id')
    return get_my_interests(student_id)

@module_router.route('/get_students_having_same_interest', methods=['GET'])
def get_students_having_same_interest_route():
    my_interests = request.args.get('my_interests')
    my_student_id = request.args.get('my_student_id')
    return get_students_having_same_interest(my_interests, my_student_id)

@module_router.route('/get_career_info', methods=['GET'])
def get_career_info_route():
    user_id = request.args.get('student_id')
    return get_career_info(user_id)

@module_router.route('/get_search_user', methods=['GET'])
def get_search_user_route():
    text = request.args.get('search_text')
    return get_search_user(text)

@module_router.route('/get_student_interest', methods=['GET'])
def get_student_interest_route():
    user_id = request.args.get('user_id')
    return get_student_interest(user_id)

@module_router.route('/add_student_interest', methods=['POST'])
def add_student_interest_route():
    return add_stundent_interest()

@module_router.route('/get_like_count', methods=['GET'])
def get_like_count_route():
    post_id = request.args.get('post_id')
    return get_like_count(post_id)

@module_router.route('/get_bookmark_status', methods=['GET'])
def get_bookmark_status_route():
    user_id = request.args.get('user_id')
    post_id = request.args.get('post_id')
    return get_bookmark_status(user_id, post_id)

@module_router.route('/get_like_status', methods=['GET'])
def get_like_status_route():
    user_id = request.args.get('user_id')
    post_id = request.args.get('post_id')
    return get_like_status(user_id, post_id)