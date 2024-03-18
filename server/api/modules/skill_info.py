from flask import jsonify, request
from .execute_query import exec_query

# 学生の特技情報を取得
def get_skill_info(user_id):
    try:
        query = """
            SELECT student_skill_t.student_id, student_skill_t.skill_id, skill_t.skill_name, student_skill_t.skill_text, skill_t.skill_icon
            FROM student_skill_t
            JOIN skill_t ON student_skill_t.skill_id = skill_t.skill_id
            WHERE student_skill_t.student_id = %s
        """
        params = (user_id,)

        result = exec_query(query, params)

        if result:
            skills = []
            for row in result:
                skill_info = {
                    'skill_id': row['skill_id'],
                    'skill_name': row['skill_name'],
                    'skill_text': row['skill_text'],
                    'skill_icon': row['skill_icon'],
                }
                skills.append(skill_info)
            return jsonify(skills)
        else:
            return jsonify({'error': 'Student not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 学生の特技を追加
def add_skill_info():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        skill_name = data.get('skill_name')
        skill_text = data.get('skill_text')

        # 特技がDBに存在するか確認
        check_query = "SELECT skill_id FROM skill_t WHERE skill_name = %s"
        check_params = (skill_name,)
        check_result = exec_query(check_query, check_params)

        query = ""
        params = ()

        if check_result:
            skill_id = check_result[0]['skill_id']
            params = (student_id, skill_id, skill_text)
            query = """
                INSERT INTO student_skill_t (student_id, skill_id, skill_text)
                VALUES (%s, %s, %s)
            """
        else:
            # skill_icon は自動生成された画像
            skill_icon = "path"
            _params = (skill_name, skill_icon)
            _query = """
                INSERT INTO skill_t (skill_name, skill_icon)
                VALUES (%s, %s)
            """
            # skill_t に登録
            exec_query(_query, _params, fetch_all=False)

            _check_query = "SELECT skill_id FROM skill_t WHERE skill_name = %s"
            _check_params = (skill_name,)
            _check_result = exec_query(_check_query, _check_params)
            skill_id = _check_result[0]['skill_id']

            # student_skill_t に登録
            params = (student_id, skill_id, skill_text)
            query = """
                INSERT INTO student_skill_t (student_id, skill_id, skill_text)
                VALUES (%s, %s, %s)
            """
            
        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data added successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 400
