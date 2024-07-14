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

        query = '''
            INSERT INTO student_info_t (
                student_id, profile_image, handle_name, first_name, family_name, sex_code, area_code
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s
            )
        '''

        params = (
            student_id, profile_image, nickname, first_name, last_name, gender, residence
        )

        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data added successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400