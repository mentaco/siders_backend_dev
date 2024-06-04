from flask import jsonify
from .execute_query import exec_query

# ユーザのプロフィール画像のパスを取得する関数
def get_user_profile_image_path(user_id):
    try:
        query = "SELECT profile_image FROM student_info_t WHERE student_id = %s"
        params = (user_id,)
        result = exec_query(query, params, fetch_all=True)

        if result:
            userProfileImagePath = result[0]['profile_image']
            print(userProfileImagePath)
            return jsonify({'profile_image': userProfileImagePath})
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500