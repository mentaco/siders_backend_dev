from flask import jsonify, request
from .execute_query import exec_query

# 学生のスキル情報を取得
def get_skill_info(user_id):
    try:
        query = """
            SELECT student_skill_t.student_id, skill_t.skill_name, student_skill_t.skill_text, skill_t.skill_icon
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
                    'skill_name': row['skill_name'],
                    'skill_text': row['skill_text'],
                    'skill_icon': row['skill_icon']
                }
                skills.append(skill_info)
            return jsonify(skills)
        else:
            return jsonify({'error': 'Student not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
