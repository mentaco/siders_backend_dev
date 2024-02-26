from flask import jsonify, request
from .execute_query import exec_query

#フォロワーリストを取得する関数
def get_follower_info(user_id):
    try:
        query = "SELECT user_id_from, relation_code FROM user_relation_t WHERE user_id_to = %s AND relation_code = 0"
        params = (user_id,)
        result = exec_query(query, params)
        if result:
            follower_list = []
            for row in result:
                follower_list.append(row['user_id_from'])
            return jsonify(follower_list)
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500