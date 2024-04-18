from flask import jsonify
from .execute_query import exec_query

#投稿のいいね数を取得する関数
def get_like_count(post_id):
    post_id = int(post_id)
    try:
        params = (post_id,)
        query = 'SELECT COUNT(*) FROM liked_post_t WHERE post_id = 1'
        result = exec_query(query, params, fetch_all=True)
        return jsonify({'data':result[0]['count']})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    