from flask import Flask
from flask import jsonify
from .execute_query import exec_query

app = Flask(__name__)

#ブックマークされた投稿のIDのリストを取得する関数
def get_bookmarked_post_ids(student_id):

    with app.app_context():
        try:
            query = """
            SELECT
                post_id
            FROM
                bookmarked_post_t
            WHERE
                user_id = %s
            """

            result = exec_query(query, params=(student_id), fetch_all=True)

            result_list = [row[0] for row in result]

            # 結果をJSON形式で返す
            return jsonify({'data': result_list})
        
        except Exception as e:
            return jsonify({'error': str(e)})



#ブックマークされた投稿を取得する関数
def get_bookmarked_posts(post_ids, focus_time=None):

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
                AND tt.hidden_status = 0
                AND tt.post_id = ANY (%s)
            """

            # focus_timeが与えられた場合の条件を追加
            if focus_time is not None:
                query += " AND tt.timeline_created_at > %s"

            # クエリに追加して下から5つの結果を抽出する
            query += " ORDER BY tt.timeline_created_at DESC LIMIT 5"

            # クエリ実行
            if focus_time is not None:
                result = exec_query(query, params=(post_ids, focus_time), fetch_all=True)
            else:
                result = exec_query(query, params=(post_ids), fetch_all=True)

            # 結果を格納するリスト
            result_list = []

            for row in result:  
                # 辞書から値のみを含むリストに変換して追加
                result_list.append(list(row.values()))

            # 最後の要素のtimeline_created_atを取得
            last_timeline_created_at = result_list[0][3] # 3はtimeline_created_atのインデックス

            # 結果をJSON形式で返す
            return jsonify({'data': result_list, 'last_timeline_created_at': last_timeline_created_at})

        except Exception as e:
            return jsonify({'error': str(e)})