from flask import Flask
from .execute_query import exec_query
from datetime import datetime

app = Flask(__name__)

# フォローリストを取得する関数
def get_follow_list(user_id_from):
    with app.app_context():
        try:
            params = (user_id_from,)
            query = 'SELECT user_id_to FROM user_relation_t WHERE user_id_from = %s AND relation_code =0'
            result = exec_query(query, params, fetch_all=True)

            # RealDictRowを辞書に変換してリストに格納
            result_list = [dict(row)['user_id_to'] for row in result]
            return result_list
        except Exception as e:
            return {'error': str(e)}, 500


# フォロー中のユーザの投稿を新しい順に取得する関数(初回呼び出し、上に引っ張って更新)
def get_followed_users_post_new(students_list, focus_time=None):

    with app.app_context():
        try:
            # クエリの基本部分
            query = """
            SELECT 
                si.student_id,
                si.handle_name,
                si.profile_image,
                tt.timeline_created_at,
                tt.post_body
            FROM 
                student_info_t si
            JOIN 
                timeline_t tt ON si.student_id = tt.user_id
            WHERE 
                tt.reply_to IS NULL
                AND tt.hidden_status = 0
                AND si.student_id = ANY (%s)
            """

            # focus_timeが与えられた場合の条件を追加
            if focus_time is not None:
                query += " AND tt.timeline_created_at > %s"

            # クエリに追加して下から5つの結果を抽出する
            query += " ORDER BY tt.timeline_created_at DESC LIMIT 5"

            # クエリ実行
            if focus_time is not None:
                result = exec_query(query, params=(students_list, focus_time), fetch_all=True)
            else:
                result = exec_query(query, params=(students_list,), fetch_all=True)

            # 結果を格納するリスト
            result_list = []

            for row in result:  
                # 辞書から値のみを含むリストに変換して追加
                result_list.append(list(row.values()))
                # 一要素ごとに改行して表示
                print(result_list[-1])
                print()

            if len(result_list) != 0:
                # 最後の要素のtimeline_created_atを返す。これをプロバイダに保持させておく。
                last_timeline_created_at = result_list[0][3]  # 3はtimeline_created_atのインデックス
                return last_timeline_created_at

        except Exception as e:
            print({'error': str(e)})

# 以前のユーザの投稿を取得する関数(下に引っ張って更新)
def get_followed_users_post_old(students_list, focus_time):

    with app.app_context():
        try:
            query = """
            SELECT 
                si.student_id,
                si.handle_name,
                si.profile_image,
                tt.timeline_created_at,
                tt.post_body
            FROM 
                student_info_t si
            JOIN 
                timeline_t tt ON si.student_id = tt.user_id
            WHERE 
                tt.reply_to IS NULL
                AND tt.hidden_status = 0
                AND si.student_id = ANY (%s)
                AND tt.timeline_created_at < %s
            ORDER BY tt.timeline_created_at DESC LIMIT 5
            """

            # クエリ実行
            result = exec_query(query, params=(students_list, focus_time), fetch_all=True)

            # 結果を格納するリスト
            result_list = []

            for row in result:  
                # 辞書から値のみを含むリストに変換して追加
                result_list.append(list(row.values()))
                # 一要素ごとに改行して表示
                print(result_list[-1])
                print()

            if len(result_list) != 0:
                # 最後の要素のtimeline_created_atを返す。これをプロバイダに保持させておく。
                last_timeline_created_at = result_list[-1][3]  # 3はtimeline_created_atのインデックス
                return last_timeline_created_at

        except Exception as e:
            print({'error': str(e)})


# main処理
def timeline_followed(user_id_from):
    with app.app_context():
        follow_list = get_follow_list(user_id_from)
        #print(follower_list)

        #年月日時分のフォーマットを揃える
        focus_time = datetime(2024,1,18,9,00)
        #a = get_followed_users_post_new(follower_list,focus_time)
        # a = get_followed_users_post_new(follower_list)
        b = get_followed_users_post_old(follow_list,focus_time)
        print(b)



# このスクリプトが直接実行された場合のみ、Flaskアプリケーションを起動する
if __name__ == "__main__":
    timeline_followed("S0000001")
