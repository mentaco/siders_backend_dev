from flask import jsonify, request
from .execute_query import exec_query

# データを取得する関数の例
def get_search_user(search_text):
    try:
        params = ('%' + search_text + '%', '%' + search_text + '%')
        query = """
        SELECT student_id, handle_name, header_image
        FROM student_info_t
        WHERE student_id LIKE %s
        OR handle_name LIKE %s;
        """
        result = exec_query(query, params)
        return jsonify({'data': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



