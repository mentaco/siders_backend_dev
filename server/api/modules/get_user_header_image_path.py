from flask import jsonify
from .execute_query import exec_query

# ユーザのヘッダー画像のパスを取得する関数
def get_user_header_image_path(user_id):
    try:
        query = "SELECT header_image FROM student_info_t WHERE student_id = %s"
        params = (user_id,)
        result = exec_query(query, params, fetch_all=True)

        if result:
            userHeaderImagePath = result[0]['header_image']
            return jsonify({'header_image': userHeaderImagePath})
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500