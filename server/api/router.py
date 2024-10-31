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

@module_router.route('/read_message', methods=['POST'])
def read_message_route():
    return read_message()

@module_router.route('/get_notice_data', methods=['GET'])
def get_notice_data_route():
    arg1 = request.args.get('user_id')
    return get_notice_data(arg1)

@module_router.route('/get_student_id', methods=['GET'])
def get_student_id_route():
    email = request.args.get('mail_address')
    return get_student_id(email)

@module_router.route('/student_profile', methods=['GET'])
def get_student_profile_route():
    student_id = request.args.get('student_id')
    return get_student_profile(student_id)

@module_router.route('/student_profile', methods=['PUT'])
def update_student_profile_route():
    return update_student_profile()

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

@module_router.route('/get_new_posts', methods=['GET'])
def get_new_posts_route():
    students_list = request.args.get('students_list')
    focus_time = request.args.get('focus_time')
    return get_new_posts(students_list,focus_time)

@module_router.route('/get_past_posts', methods=['GET'])
def get_users_past_posts_route():
    students_list = request.args.get('students_list')
    focus_time = request.args.get('focus_time')
    return get_past_posts(students_list,focus_time)

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
    my_student_id = request.args.get('my_student_id')
    return get_search_user(text,my_student_id)

@module_router.route('/add_student', methods=['POST'])
def add_student():
    return add_student()    

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

@module_router.route('/post_liked_user_info', methods=['POST'])
def add_liked_user_route():
    return add_liked_user()

@module_router.route('/post_liked_user_info', methods=['DELETE'])
def del_liked_user_route():
    return del_liked_user()

@module_router.route('/post_bookmarked_user_info', methods=['POST'])
def add_bookmarked_user_route():
    return add_bookmarked_user()

@module_router.route('/post_bookmarked_user_info', methods=['DELETE'])
def del_bookmarked_user_route():
    return del_bookmarked_user()

@module_router.route('/get_timeline_comment', methods=['GET'])
def get_timeline_comment_route():
    post_id = request.args.get('post_id')
    focus_time = request.args.get('focus_time')
    return get_timeline_comment(post_id, focus_time)

@module_router.route('/get_follow_count', methods=['GET'])
def get_follow_count_route():
    student_id = request.args.get('student_id')
    return get_follow_count(student_id)

@module_router.route('/get_follower_count', methods=['GET'])
def get_follower_count_route():
    student_id = request.args.get('student_id')
    return get_follower_count(student_id)

@module_router.route('/get_user_name', methods=['GET'])
def get_user_name_route():
    student_id = request.args.get('student_id')
    return get_user_name(student_id)

@module_router.route('/get_user_profile_image_path', methods=['GET'])
def get_user_profile_image_path_route():
    student_id = request.args.get('student_id')
    return get_user_profile_image_path(student_id)

@module_router.route('/get_user_header_image_path', methods=['GET'])
def get_user_header_image_path_route():
    student_id = request.args.get('student_id')
    return get_user_header_image_path(student_id)

@module_router.route('/get_scout_ids', methods=['GET'])
def get_scout_ids_route():
    student_id = request.args.get('student_id')
    return get_scout_ids(student_id)

@module_router.route('/get_scout_list', methods=['GET'])
def get_scout_list_route():
    scout_ids = request.args.get('scout_ids')
    return get_scout_list(scout_ids)

@module_router.route('/get_work_ids', methods=['GET'])
def get_work_ids_route():
    student_id = request.args.get('student_id')
    return get_work_ids(student_id)

@module_router.route('/get_work_list', methods=['GET'])
def get_work_list_route():
    work_ids = request.args.get('work_ids')
    return get_work_list(work_ids)

@module_router.route('/get_bookmark_post_ids', methods=['GET'])
def get_bookmarked_post_ids_route():
    user_id = request.args.get('user_id')
    return get_bookmarked_post_ids(user_id)

@module_router.route('/get_bookmark_list', methods=['GET'])
def get_bookmarked_posts_route():
    post_ids = request.args.get('post_ids')
    return get_bookmarked_posts(post_ids)

@module_router.route('/add_user_info', methods=['POST'])
def add_user_info():
    return add_user_info()

@module_router.route('/add_auth_info',methods=['POST'])
def add_auth_info():
    return add_auth_info()

@module_router.route('add_interest_info', methods=['POST'])
def add_interest_info():
    return add_interest_info()

@module_router.route('/get_other_user_info', methods=['GET'])
def get_other_user_info_route():
    user_id = request.args.get('user_id')
    return get_other_user_info(user_id)

@module_router.route('/get_company_info', methods=['GET'])
def get_company_info_route():
    user_id = request.args.get('user_id')
    return get_company_info(user_id)