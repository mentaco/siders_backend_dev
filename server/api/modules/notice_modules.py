from flask import jsonify, request
from .execute_query import exec_query

# 通知を取得する関数
def get_notice_data(user_id):
    params = (user_id,)
    try:
        query = ("""
SELECT
  CASE
    WHEN LEFT(m.message_from, 1) = 'S' THEN s.handle_name
    WHEN LEFT(m.message_from, 1) = 'C' THEN c.company_name
    ELSE NULL
  END AS from_name,
  CASE
    WHEN LEFT(m.message_from, 1) = 'S' THEN s.profile_image
    WHEN LEFT(m.message_from, 1) = 'C' THEN c.company_logomark
    ELSE NULL
  END AS from_image,
  m.message_from,
  m.message_type_code,
  m.message_created_at
FROM
  message_t m
LEFT JOIN
  student_info_t s ON LEFT(m.message_from, 1) = 'S' AND m.message_from = s.student_id
LEFT JOIN
  company_info_t c ON LEFT(m.message_from, 1) = 'C' AND m.message_from = c.company_id
WHERE
  m.message_to = %s
                 """)
        result = exec_query(query,params)
        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
