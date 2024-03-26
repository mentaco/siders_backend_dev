from flask import jsonify
from .execute_query import exec_query

#フォローリストを取得する関数
def get_follow_info(user_id):
    try:
        query = """
            SELECT user_relation_t.user_id_to, user_relation_t.relation_code,
            student_info_t.handle_name, student_info_t.profile_image
            FROM user_relation_t
            JOIN student_info_t ON user_relation_t.user_id_to = student_info_t.student_id
            WHERE user_relation_t.user_id_from = %s
        """
        params = (user_id,)
        result = exec_query(query, params)
        if result:
            return jsonify(result)
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
