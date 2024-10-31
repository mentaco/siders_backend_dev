from flask import Flask
from .execute_query import exec_query
from flask import jsonify
from .timeline_disp_followed_post import get_follow_list
import json

app = Flask(__name__)


#生徒の興味のある職を表す文字列を要素ごとに分割する関数
def divide_student_interests(input_strings):
    divided_list = []

    for i in range(0, len(input_strings) - 2, 3):
        if i + 2 < len(input_strings):
            triplet = input_strings[i:i + 3]
            divided_list.append(triplet)

    return divided_list


#自分の興味のある項目を取得する関数
def get_my_interests(student_id):
    with app.app_context():
        try:
            params = (student_id,)
            query = 'SELECT student_interest FROM student_info_t WHERE student_id = %s'
            result = exec_query(query, params, fetch_all=True)

            if result:
                my_interest = result[0]['student_interest']
            else:
                my_interest = ''


            return jsonify({'data': my_interest})  # データをJSON形式で返す

        except Exception as e:
            return jsonify({'error': str(e)}), 500

        

#自分がフォローしている学生をのぞいた、興味が被っている学生を取得する関数
def get_students_having_same_interest(my_interests, my_student_id):
    with app.app_context():
        try:
            # 興味が被っている学生のstudent_idを格納するセット
            same_interest_students = set()

            my_interests = divide_student_interests(my_interests)

            # 各興味について、興味が被っている学生を検索する
            for interest in my_interests:
                query = """
                    SELECT DISTINCT si.student_id 
                    FROM student_info_t si 
                    JOIN user_relation_t ur ON si.student_id = ur.user_id_to 
                    WHERE  ur.user_id_from = %s
                    AND relation_code != 2
                    AND student_interest LIKE %s
                """
   
                params = (my_student_id,'%' + interest + '%',)  # 部分一致のために%を付ける
                result = exec_query(query, params, fetch_all=True)

                # 検索結果からstudent_idをセットに追加
                for row in result:
                    if my_student_id is not None and row['student_id'] == my_student_id:
                        continue
                    same_interest_students.add(row['student_id'])
            
            # student_idの降順に並び替え
            same_interest_students_list = sorted(list(same_interest_students))


            # 自分のフォローしているユーザのリストを取得
            res = get_follow_list(my_student_id).data

            res_data = json.loads(res)

            my_followed_students = res_data['data']

            # my_followed_studentsに含まれる要素をsorted_studentsから削除
            same_interest_students_list = [student_id for student_id in same_interest_students_list if student_id not in my_followed_students]

            return jsonify({'data': same_interest_students_list})
        

        except Exception as e:
            return jsonify({'error': str(e)}), 500

