from flask import Flask
from .execute_query import exec_query
from datetime import datetime
from .timeline_disp_followed_post import get_follow_list, get_followed_users_post_old, get_followed_users_post_new

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

            # RealDictRowを辞書に変換してリストに格納
            if result:
                my_interest = result[0]['student_interest']
            else:
                my_interest = ''

            #興味のある業種列を要素分解
            my_interest = divide_student_interests(my_interest)

            return my_interest
        
        except Exception as e:
            return {'error': str(e)}, 500
        

#自分がフォローしている学生をのぞいた、興味が被っている学生を取得する関数
def get_students_having_same_interest(my_interests, my_student_id):
    with app.app_context():
        try:
            # 興味が被っている学生のstudent_idを格納するセット
            same_interest_students = set()

            # 各興味について、興味が被っている学生を検索する
            for interest in my_interests:
                query = "SELECT DISTINCT student_id FROM student_info_t WHERE student_interest LIKE %s"
                params = ('%' + interest + '%',)  # 部分一致のために%を付ける
                result = exec_query(query, params, fetch_all=True)

                # 検索結果からstudent_idをセットに追加
                for row in result:
                    if my_student_id is not None and row['student_id'] == my_student_id:
                        continue
                    same_interest_students.add(row['student_id'])
            
            # student_idの降順に並び替え
            same_interest_students_list = sorted(list(same_interest_students))

            # 自分のフォローしているユーザのリストを取得
            my_followed_students = get_follow_list(my_student_id)

            # my_followed_studentsに含まれる要素をsorted_studentsから削除
            same_interest_students_list = [student_id for student_id in same_interest_students_list if student_id not in my_followed_students]

            return same_interest_students_list

        except Exception as e:
            print({'error': str(e)})
        

# このスクリプトが直接実行された場合のみ、Flaskアプリケーションを起動する
if __name__ == "__main__":
    a = get_my_interests("S0000001")

    b = get_students_having_same_interest(a,"S0000001")

    c = get_followed_users_post_new()

    d = get_followed_users_post_old()

