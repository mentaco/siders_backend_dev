from flask import jsonify
from .execute_query import exec_query

#投稿のいいね数を取得する関数
def get_like_count(post_id):
    try:
        query = """
        SELECT COUNT(*)
        FROM liked_post_t
        WHERE post_id = %s;
        """
        params = (post_id,)
        result = exec_query(query, params)
        if result:
            return jsonify(result)
        else:
            return jsonify({'error': 'Post not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500