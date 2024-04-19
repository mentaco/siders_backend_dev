from flask import jsonify
from .execute_query import exec_query

#ログインユーザがタイムライン上で、該当投稿をいいねしているかどうかを取得する関数
def get_like_status(user_id, post_id):
    post_id = int(post_id)
    try:
        params = (user_id, post_id)
        query = 'SELECT COUNT(*) FROM liked_post_t WHERE user_id = %s AND post_id = %s'
        result = exec_query(query, params, fetch_all=True)
        if result[0]['count'] == 1:
            return jsonify({'data':True})
        else:
            return jsonify({'data':False})
            

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    