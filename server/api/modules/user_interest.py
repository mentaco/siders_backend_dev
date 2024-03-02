from flask import jsonify, request
from .execute_query import exec_query

#user_idから学生の興味の分野を取ってくる関数
def get_student_interest(user_id):
    try:
        query = ('SELECT student_interest FROM student_info_t WHERE student_info_t.student_id = %s')
        params = (user_id,)
        result = exec_query(query,params)

        return jsonify({'data': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# ユーザの興味のある分野を更新する関数の例
def add_stundent_interest():
    try:

        data = request.get_json()
        user_id = data.get('user_id')
        student_interest = data.get('student_interest')

        params = (student_interest,user_id,)
        query = 'UPDATE student_info_t SET student_interest = %s WHERE student_info_t.student_id = %s'

        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data added successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400