from flask import jsonify
from .execute_query import exec_query

# フォロー数を取得する関数
def get_follow_count(user_id):
    try:
        query = "SELECT COUNT(user_id_to) FROM user_relation_t WHERE user_id_from = %s AND relation_code = 0"
        params = (user_id,)
        result = exec_query(query, params, fetch_all=True)
        return jsonify(result[0])

    except Exception as e:
        return jsonify({'error': str(e)}), 500
