from flask import jsonify, request
from .execute_query import exec_query

# マイページの情報取得
def get_mypage_info(user_id):
    try:
        query = """
            SELECT handle_name, faculty, header_image, profile_image, motto, 
                student_intro, web_link, post_num, avg_portfolio, family_name, first_name
            FROM student_info_t
            WHERE mail_address = %s
        """

        params = (user_id,)

        result = exec_query(query, params)

        if result:
            student_info = result[0]
            return jsonify(student_info)
        else:
            return jsonify({'error': 'User not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500