from flask import jsonify
from .execute_query import exec_query

def get_career_info(student_id):
    try:
        query = """
            SELECT career_id, affiliation_id, career_title, career_detail, career_start_at, career_end_at,
                publication_status, career_type_code, result_num, career_image_1, career_image_2, career_image_3
            FROM career_info_t
            WHERE student_id = %s
        """
        params = (student_id,)

        result = exec_query(query, params)

        if result:
            return jsonify(result)
        else:
            return jsonify({'error': 'Career information not found for the specified student ID'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
