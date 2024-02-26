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
    WHEN LEFT(m.message_from, 1) = 'C' THEN c.company_header_image
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
# # データを挿入する関数の例
# def example_add_data():
#     try:
#         # シーケンスの取得
#         seq = exec_query("SELECT NEXTVAL('skill_id_seq')")[0]['nextval']
#         data = request.get_json()
#         skill_id = seq
#         skill_name = data.get('skill_name')
#         skill_icon = data.get('skill_icon')
#         params = (skill_id, skill_name, skill_icon)
#         query = 'INSERT INTO skill_t (skill_id, skill_name, skill_icon) VALUES (%s, %s, %s)'
#         exec_query(query, params, fetch_all=False)
#         return jsonify({'message': 'Data added successfully'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400
# # データを削除する関数の例
# def example_del_data():
#     try:
#         data = request.get_json()
#         skill_id = data.get('skill_id')
#         params = (skill_id,)
#         query = 'DELETE FROM skill_t WHERE skill_id = %s'
#         result = exec_query(query, params, fetch_all=False)
#         return jsonify({'message': 'Data deleted successfully'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500