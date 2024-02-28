from flask import jsonify, request
from .execute_query import exec_query

#フォローリストを取得する関数
def get_follow_info(user_id):
    try:
        query = "SELECT user_id_to, relation_code FROM user_relation_t WHERE user_id_from = %s AND relation_code = 0"
        params = (user_id,)
        result = exec_query(query, params)
        if result:
            follow_list = []
            for row in result:
                follow_list.append(row['user_id_to'])
            return jsonify(follow_list)
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
