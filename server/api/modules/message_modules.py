from flask import jsonify, request
from .execute_query import exec_query
# user_idに関連するメッセージを取得する関数
def get_message(user_id):
    try:
        params = (user_id,)*14
        query = ("""
    SELECT
        m.message_id,
        m.message_from,
        m.message_to,
        m.message_body,
        m.message_status_code,
        m.message_created_at,
        CASE
            WHEN m.message_from = %s AND LEFT(m.message_to, 1) = 'S' THEN s_to_handle.handle_name
            WHEN m.message_from = %s  AND LEFT(m.message_to, 1) = 'C' THEN c_to_info.company_name
            WHEN LEFT(m.message_from, 1) = 'S' AND m.message_to = %s THEN s_handle.handle_name
            WHEN LEFT(m.message_from, 1) = 'C' AND m.message_to = %s THEN c_info.company_name
        END AS from_name,
        CASE
            WHEN m.message_to = %s AND LEFT(m.message_from, 1) = 'S' THEN s_handle.handle_name
            WHEN m.message_to = %s AND LEFT(m.message_from, 1) = 'C' THEN c_info.company_name
            WHEN LEFT(m.message_to, 1) = 'S' AND m.message_from = %s THEN s_to_handle.handle_name
            WHEN LEFT(m.message_to, 1) = 'C' AND m.message_from = %s THEN c_to_info.company_name
        END AS to_name,
        CASE
            WHEN m.message_from = %s AND LEFT(m.message_to, 1) = 'S' THEN s_to_handle.profile_image
            WHEN m.message_from = %s AND LEFT(m.message_to, 1) = 'C' THEN c_to_info.company_header_image
            WHEN LEFT(m.message_from, 1) = 'S' AND m.message_to = %s THEN s_handle.profile_image
            WHEN LEFT(m.message_from, 1) = 'C' AND m.message_to = %s THEN c_info.company_header_image
        END AS recipient_image
    FROM
        message_t m
    LEFT JOIN
        student_info_t s_handle ON m.message_from = s_handle.student_id
    LEFT JOIN
        student_info_t s_to_handle ON m.message_to = s_to_handle.student_id
    LEFT JOIN
        company_info_t c_info ON m.message_from = c_info.company_id
    LEFT JOIN
        company_info_t c_to_info ON m.message_to = c_to_info.company_id
    WHERE
        m.message_from = %s OR m.message_to = %s
                 """)
        result = exec_query(query,params)
        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# メッセージデータを挿入する関数
def add_message():
    try:
        # シーケンスの取得
        data = request.get_json()
        message_from = data.get('message_from')
        message_to = data.get('message_to')
        message_type_code = data.get('message_type_code')
        message_body = data.get('message_body')
        message_status_code = data.get('message_status_code')
        message_created_at = data.get('message_created_at')
        params = (message_from,message_to,message_type_code,message_body,message_status_code,message_created_at)
        query = 'INSERT INTO message_t (message_from, message_to, message_type_code, message_body, message_status_code, message_created_at) VALUES (%s, %s, %s,%s,%s,%s)'
        exec_query(query, params, fetch_all=False)
        return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

