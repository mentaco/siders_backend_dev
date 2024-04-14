from flask import jsonify, request
from .execute_query import exec_query

#ユーザ関係を取得する関数
def get_user_relation(user_id_from,user_id_to):
    try:
        params = (user_id_from, user_id_to)
        query = 'SELECT relation_code FROM user_relation_t WHERE user_id_from = %s AND user_id_to = %s'
        result = exec_query(query, params, fetch_all=True)
        print(params)
        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# フォローリクエストを送信する関数
def follow_request_add():
    try:
        data = request.get_json()
        user_id_from = data.get('user_id_from')
        user_id_to = data.get('user_id_to')
        relation_code = data.get('relation_code')

        params = (user_id_from, user_id_to, relation_code)
        query = 'INSERT INTO user_relation_t (user_id_from, user_id_to, relation_code) VALUES (%s, %s, %s)'

        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data added successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# ユーザ関係を削除する(未フォローの状態にする)関数
def user_relation_del():
    try:
        data = request.get_json()
        user_id_from = data.get('user_id_from')
        user_id_to = data.get('user_id_to')

        params = (user_id_from,user_id_to)
        query = 'DELETE FROM user_relation_t WHERE user_id_from = %s AND user_id_to = %s'

        result = exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

