from flask import jsonify, request
from .execute_query import exec_query

def get_search_user(search_text, my_student_id):
    try:
        params = ('%' + search_text + '%', '%' + search_text + '%', my_student_id)
        query = """
        SELECT si.student_id, si.handle_name, si.header_image, rt.relation_code
        FROM student_info_t si
        LEFT JOIN user_relation_t rt ON si.student_id = rt.user_id_to
        WHERE (si.student_id LIKE %s OR si.handle_name LIKE %s)
        AND si.student_id != %s
        AND rt.user_id_from = %s;
        """
        result = exec_query(query, params + (my_student_id,))
        return jsonify({'data': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


