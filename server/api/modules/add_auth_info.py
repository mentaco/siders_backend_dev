from flask import jsonify, request
from .execute_query import exec_query

def add_auth_info():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        univ_name = data.get('univ_name', '')
        faculty = data.get('faculty', '')
        department = data.get('department', '')
        birthday = data.get('birthday', '')
        expected_graduation = data.get('expected_graduation', '')

        check_query = 'SELECT * FROM student_info_t WHERE user_id = %s'
        existing_user = exec_query(check_query, (user_id,))

        if existing_user:
            update_query = '''
                UPDATE student_info_t
                SET univ_name = %s,
                    faculty = %s,
                    department = %s,
                    birthday = %s,
                    expected_graduation = %s
                WHERE user_id = %s
            '''
            params = (
                univ_name, faculty, department, birthday, expected_graduation, user_id
            )
            exec_query(update_query, params, fetch_all=False)
            message = 'Data updated successfully'
        else:
            insert_query = '''
                INSERT INTO student_info_t (
                    user_id, univ_name, faculty, department, birthday, expected_graduation
                ) VALUES (
                    %s, %s, %s, %s, %s, %s
                )
            '''
            params = (
                user_id, univ_name, faculty, department, birthday, expected_graduation
            )
            exec_query(insert_query, params, fetch_all=False)
            message = 'Data added successfully'

        return jsonify({'message': message})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
