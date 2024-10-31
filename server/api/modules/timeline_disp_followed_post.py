from flask import Flask
from flask import jsonify
from .execute_query import exec_query

app = Flask(__name__)

#学生リストの文字列を分割する関数
def divide_students_list(input_strings):
    divided_list = []

    for i in range(0, len(input_strings), 8):
        chunk = input_strings[i:i + 8]
        divided_list.append(chunk)

    return divided_list


# フォローリストを取得する関数
def get_follow_list(user_id_from):
    with app.app_context():
        try:
            params = (user_id_from,)
            query = "SELECT user_id_to FROM user_relation_t WHERE user_id_from = %s AND relation_code = 0"
            result = exec_query(query, params, fetch_all=True)

            # クエリの結果をリスト形式に変換して返す
            follow_list = [row['user_id_to'] for row in result]

            return jsonify({'data': follow_list})
        except Exception as e:
            return jsonify({'error': str(e)}), 500


def get_new_posts(students_list, focus_time=None):

    students_list = divide_students_list(students_list)

    with app.app_context():
        try:
            # クエリの基本部分
            query = """
            SELECT 
                si.student_id,
                si.handle_name,
                si.profile_image,
                tt.timeline_created_at,
                tt.post_body,
                tt.post_id
            FROM 
                student_info_t si
            JOIN 
                timeline_t tt ON si.student_id = tt.user_id
            WHERE 
                tt.reply_post_id IS NULL
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

            if result == []:
                return jsonify({'message': '新しい投稿はありません'})

            # 結果を格納するリスト
            result_list = []

            for row in result:  
                # 辞書から値のみを含むリストに変換して追加
                result_list.append(list(row.values()))

            # 取得した中で、最新の投稿時間を取得
            latest_post_created_at = result_list[-1][3] # 3はtimeline_created_atのインデックス

            # 結果をJSON形式で返す
            return jsonify({'data': result_list, 'latest_post_created_at': latest_post_created_at})

        except Exception as e:
            return jsonify({'error': str(e)})


# 以前のユーザの投稿を取得する関数(下に引っ張って更新)
def get_past_posts(students_list, focus_time):

    students_list = divide_students_list(students_list)

    with app.app_context():
        try:
            query = """
            SELECT 
                si.student_id,
                si.handle_name,
                si.profile_image,
                tt.timeline_created_at,
                tt.post_body,
                tt.post_id
            FROM 
                student_info_t si
            JOIN 
                timeline_t tt ON si.student_id = tt.user_id
            WHERE 
                tt.reply_post_id IS NULL
                AND tt.hidden_status = 0
                AND si.student_id = ANY (%s)
                AND tt.timeline_created_at < %s
            ORDER BY tt.timeline_created_at DESC LIMIT 5
            """

            # クエリ実行
            result = exec_query(query, params=(students_list, focus_time), fetch_all=True)

            if result == []:
                return jsonify({'message': '投稿を全て表示しました'})

            # 結果を格納するリスト
            result_list = []

            for row in result:  
                # 辞書から値のみを含むリストに変換して追加
                result_list.append(list(row.values()))

             # 取得した中で最も遅い時間に投稿されたの投稿時間を取得
            oldest_post_created_at = result_list[-1][3]  # 3はtimeline_created_atのインデックス

             # 取得した中で最新のtimeline_created_atを返す。
            latest_post_created_at = result_list[0][3]  # 3はtimeline_created_atのインデックス
            
            return jsonify({'data': result_list, 'oldest_post_created_at': oldest_post_created_at, 'latest_post_created_at': latest_post_created_at})

        except Exception as e:
            return jsonify({'error': str(e)})
        