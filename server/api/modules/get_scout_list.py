from flask import jsonify
from .execute_query import exec_query

# 自分が受けているスカウトIDを取得する関数
def get_scout_ids(user_id):
    try:
        query = """
        SELECT work_or_scout_id
        FROM message_t
        WHERE message_to = %s AND work_or_scout_id IS NOT NULL;
        """
        params = (user_id,)

        result = exec_query(query, params, fetch_all=True)
        
        if result:
            # 結果からスカウトIDのリストを抽出
            scout_ids = [int(row['work_or_scout_id']) for row in result]

            return jsonify(scout_ids)
        else:
            return jsonify({'error': 'Scout not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# スカウトリストを取得する関数
def get_scout_list(scout_ids):
    try:
        if not scout_ids:
            return jsonify({'error': 'No scout IDs provided'}), 400

        # scout_ids をカンマで分割し、それぞれの要素を整数に変換
        scout_ids_list = scout_ids.split(',')
        scout_ids_int = [int(id) for id in scout_ids_list]

        results = []
        for scout_id in scout_ids_int:
            query = """
                SELECT 
                    company_info_t.company_name, 
                    company_info_t.company_logomark, 
                    scout_t.scout_body, 
                    scout_t.scout_start_at, 
                    scout_t.scout_end_at
                FROM 
                    scout_t
                JOIN 
                    company_info_t ON scout_t.company_id = company_info_t.company_id
                WHERE 
                    scout_t.scout_id = %s;
            """
            # scout_id を単一のパラメータとして渡す
            result = exec_query(query, (scout_id,), fetch_all=True)
            if result:
                results.extend(result)
        
        if results:
            return jsonify(results)
        else:
            return jsonify({'error': 'Scouts not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500