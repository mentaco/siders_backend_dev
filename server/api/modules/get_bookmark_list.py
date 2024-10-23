from flask import Flask
from flask import jsonify
from .execute_query import exec_query
import json

app = Flask(__name__)

#ブックマークされた投稿のIDのリストを取得する関数
def get_bookmarked_post_ids(user_id):

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

            result = exec_query(query, params=(user_id,), fetch_all=True)

            result_list = [row['post_id'] for row in result]

            # 結果をJSON形式で返す
            return jsonify({'data': result_list})
        
        except Exception as e:
            return jsonify({'error': str(e)})

# ブックマークされた投稿を取得する関数
def get_bookmarked_posts(post_ids):
    with app.app_context():
        try:
            post_ids = json.loads(post_ids)

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
                tt.hidden_status = 0
                AND tt.post_id = ANY (%s)
            """

            # クエリ実行
            result = exec_query(query, params=(post_ids,), fetch_all=True)

            # 結果を格納するリスト
            result_list = []

            for row in result:  
                # タプルから値のみを含むリストに変換して追加
                result_list.append(list(row.values()))

            # 結果をJSON形式で返す
            return jsonify({'data': result_list})

        except Exception as e:
            return jsonify({'error': str(e)})