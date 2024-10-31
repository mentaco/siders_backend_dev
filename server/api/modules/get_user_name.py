from flask import jsonify
from .execute_query import exec_query

# ユーザのカバー画像のパスを取得する関数
def get_user_name(user_id):
    try:
        query = "SELECT handle_name FROM student_info_t WHERE student_id = %s"
        params = (user_id,)
        result = exec_query(query, params, fetch_all=True)

        if result:
            userName = result[0]['handle_name']
            return jsonify({'handle_name': userName})
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500