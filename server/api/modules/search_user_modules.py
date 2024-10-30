from flask import jsonify, request
from .execute_query import exec_query

def get_search_user(search_text, my_student_id):
    try:
        # パラメータの設定
        params_user = (my_student_id, '%' + search_text + '%', '%' + search_text + '%', my_student_id)
        params_company = (my_student_id, '%' + search_text + '%', '%' + search_text + '%')

        query = """
        SELECT si.student_id AS id, si.handle_name AS name, si.profile_image AS image, rt.relation_code AS relation_code, 'student' AS type
        FROM student_info_t si
        LEFT JOIN user_relation_t rt ON si.student_id = rt.user_id_to AND rt.user_id_from = %s
        WHERE (si.student_id ILIKE %s OR si.handle_name ILIKE %s)
        AND si.student_id != %s
        
        UNION ALL

        SELECT ci.company_id AS id, ci.company_name AS name, ci.company_logomark AS image, rt.relation_code AS relation_code, 'company' AS type
        FROM company_info_t ci
        LEFT JOIN user_relation_t rt ON ci.company_id = rt.user_id_to AND rt.user_id_from = %s
        WHERE (ci.company_id ILIKE %s OR ci.company_name ILIKE %s);
        """
        
        # パラメータを統合
        result = exec_query(query, params_user + params_company)
        print(result)

        return jsonify({'data': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
