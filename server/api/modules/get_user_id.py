from flask import jsonify, request
from .execute_query import exec_query

# メールアドレス情報からユーザIDの取得を行う関数、ログイン処理時に使用
def get_student_id(email):
    try:
        query = "SELECT student_id FROM student_info_t WHERE email = %s"
        params = (email,)
        result = exec_query(query, params)

        if result:
            student_id = result[0]['student_id']
            return jsonify({'student_id': student_id})
        else:
            return jsonify({'error': 'User not found'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
