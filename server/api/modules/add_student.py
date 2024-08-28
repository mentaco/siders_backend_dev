from flask import jsonify, request
from .execute_query import exec_query

def add_student():
    data = request.get_json()
    
    required_fields = [
        "profile_image", "nickname", "first_name", "last_name", "gender",
        "residence", "prefecture", "student_id", "enrollment_period",
        "faculty", "department", "birthdate", "graduation_date", "interested_jobs"
    ]
    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f'Missing fields: {", ".join(missing_fields)}'}), 400

    try:
        query = """
            UPDATE student_info_t
            SET
                profile_image = %s,
                nickname = %s,
                first_name = %s,
                last_name = %s,
                gender = %s,
                residence = %s,
                prefecture = %s,
                enrollment_period = %s,
                faculty = %s,
                department = %s,
                birthdate = %s,
                graduation_date = %s,
                interested_jobs = %s
            WHERE
                student_id = %s
        """

        params = (
            data['profile_image'], data['nickname'], data['first_name'], data['last_name'], data['gender'],
            data['residence'], data['prefecture'], data['enrollment_period'],
            data['faculty'], data['department'], data['birthdate'], data['graduation_date'], data['interested_jobs'],
            data['student_id']
        )

        
        exec_query(query, params)
        return jsonify({'message': 'Student information added successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500