from flask import jsonify, request
from .execute_query import exec_query

# データを取得する関数の例
def example_get_data():
    try:
        result = exec_query('SELECT * FROM skill_t')
        return jsonify({'data': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# データを挿入する関数の例
def example_add_data():
    try:
        # シーケンスの取得
        seq = exec_query("SELECT NEXTVAL('skill_id_seq')")[0]['nextval']

        data = request.get_json()
        skill_id = seq
        skill_name = data.get('skill_name')
        skill_icon = data.get('skill_icon')

        params = (skill_id, skill_name, skill_icon)
        query = 'INSERT INTO skill_t (skill_id, skill_name, skill_icon) VALUES (%s, %s, %s)'

        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data added successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# データを削除する関数の例
def example_del_data():
    try:
        data = request.get_json()
        skill_id = data.get('skill_id')

        params = (skill_id,)
        query = 'DELETE FROM skill_t WHERE skill_id = %s'

        result = exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
