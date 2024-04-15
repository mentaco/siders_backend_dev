from flask import jsonify, request
from .execute_query import exec_query

# データを取得する関数の例
def get_search_user(search_text,my_student_id):
    try:
        params = (my_student_id, '%' + search_text + '%', '%' + search_text + '%')
        query = ("""
            SELECT
                s.student_id,
                s.handle_name,
                s.header_image,
                ur.relation_code
            FROM
                student_info_t s
            LEFT JOIN
                user_relation_t ur ON ur.user_id_to = s.student_id AND ur.user_id_from = %s
            WHERE
                s.student_id LIKE %s
                OR s.handle_name LIKE %s
        """)
        result = exec_query(query, params)
        
        # student_idがuser_idである行を除外する
        filtered_result = [row for row in result if row['student_id'] != my_student_id]
        
        return jsonify({'data': filtered_result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



