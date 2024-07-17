from flask import jsonify, request
from .execute_query import exec_query

def add_student_info():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        profile_image = data.get('profile_image', '')
        nickname = data.get('nickname', '')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        gender = data.get('gender', '')
        residence = data.get('residence', '')

        check_query = 'SELECT * FROM student_info_t WHERE student_id = %s'
        existing_student = exec_query(check_query, (student_id,))

        if existing_student:
            update_query = '''
                UPDATE student_info_t
                SET profile_image = %s,
                    handle_name = %s,
                    first_name = %s,
                    family_name = %s,
                    sex_code = %s,
                    area_code = %s
                WHERE student_id = %s
            '''
            params = (
                profile_image, nickname, first_name, last_name, gender, residence, student_id
            )
            exec_query(update_query, params, fetch_all=False)
            message = 'Data updated successfully'
        else:
            insert_query = '''
                INSERT INTO student_info_t (
                    student_id, profile_image, handle_name, first_name, family_name, sex_code, area_code
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s
                )
            '''
            params = (
                student_id, profile_image, nickname, first_name, last_name, gender, residence
            )
            exec_query(insert_query, params, fetch_all=False)
            message = 'Data added successfully'

        return jsonify({'message': message})

    except Exception as e:
        return jsonify({'error': str(e)}), 400