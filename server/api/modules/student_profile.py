from flask import jsonify, request
from .execute_query import exec_query

# マイページの情報取得
def get_student_profile(student_id):
    try:
        query = """
            SELECT handle_name, faculty, header_image, profile_image, motto, area_code,
                student_intro, web_link, post_num, avg_portfolio, family_name, first_name
            FROM student_info_t
            WHERE student_id = %s
        """

        params = (student_id,)

        result = exec_query(query, params)

        if result:
            profile = result[0]
            return jsonify(profile)
        else:
            return jsonify({'error': 'User not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def update_student_profile():
    try:
        data = request.get_json()
        contents_dict = dict()
        student_id = data.get('student_id')
        contents_dict['header_image'] = data.get('header_image')
        contents_dict['profile_image'] = data.get('profile_image')
        contents_dict['handle_name'] = data.get('handle_name')
        contents_dict['area_code'] = data.get('area_code')
        contents_dict['motto'] = data.get('motto')
        contents_dict['web_link'] = data.get('web_link')
        contents_dict['student_intro'] = data.get('student_intro')

        # 変更のあった項目の辞書
        change_contents = {key: val for key, val in contents_dict.items() if val is not None}

        contents_names = list(change_contents.keys())  # 変更のあった項目の名前

        params = list(change_contents[key] for key in contents_names)  # 変更のあった項目の値
        params.append(student_id)
        params = tuple(params)

        query = "UPDATE student_info_t SET "
        for column in contents_names:
            query += f"{column} = %s, "
        query = query[:-2]
        query += " WHERE student_id = %s"

        exec_query(query, params, fetch_all=False)

        return jsonify({'message': 'Data updated successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

