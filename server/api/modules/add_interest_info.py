from flask import jsonify, request
from .execute_query import exec_query

def add_interest_info():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        student_interest = data.get('student_interest', '')

        check_query = 'SELECT * FROM student_info_t WHERE student_id = %s'
        existing_student = exec_query(check_query, (student_id,))

        if existing_student:
            update_query = '''
                UPDATE student_info_t
                SET student_interest = %s
                WHERE student_id = %s
            '''
            params = (student_interest, student_id)
            exec_query(update_query, params, fetch_all=False)
            message = 'Data updated successfully'
        else:
            insert_query = '''
                INSERT INTO student_info_t (
                    student_id, student_interest
                ) VALUES (
                    %s, %s
                )
            '''
            params = (student_id, student_interest)
            exec_query(insert_query, params, fetch_all=False)
            message = 'Data added successfully'

        return jsonify({'message': message})

    except Exception as e:
        return jsonify({'error': str(e)}), 400
