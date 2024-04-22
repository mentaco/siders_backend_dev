from flask import jsonify, request
from .execute_query import exec_query

#投稿をいいねしたユーザを追加する関数
def add_liked_user():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        post_id = data.get('post_id')
        
        params = (post_id, user_id,)
        query = 'INSERT INTO liked_post_t(post_id, user_id) VALUES (%s, %s)'
        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data added successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

#投稿のいいねを取り消す関数
def del_liked_user():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        post_id = data.get('post_id')
        params = (post_id, user_id,)
        query = 'DELETE FROM liked_post_t WHERE post_id = %s AND user_id = %s'
        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400