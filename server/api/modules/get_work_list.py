from flask import jsonify
from .execute_query import exec_query

# 自分が受けているスカウトIDを取得する関数
def get_work_ids(user_id):
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
            work_ids = [int(row['work_or_scout_id']) for row in result]

            return jsonify(work_ids)
        else:
            return jsonify({'error': 'work not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# スカウトリストを取得する関数
def get_work_list(work_ids):
    try:
        if not work_ids:
            return jsonify({'error': 'No work IDs provided'}), 400

        # work_ids をカンマで分割し、それぞれの要素を整数に変換
        work_ids_list = work_ids.split(',')
        work_ids_int = [int(id) for id in work_ids_list]

        results = []
        for work_id in work_ids_int:
            query = """
                SELECT 
                    company_info_t.company_name, 
                    company_info_t.company_logomark, 
                    work_t.work_content, 
                    work_t.contract_start_at, 
                    work_t.contract_end_at,
                    work_t.work_title
                FROM 
                    work_t
                JOIN 
                    company_info_t ON work_t.company_id = company_info_t.company_id
                WHERE 
                    work_t.work_id = %s;
            """
            # work_id を単一のパラメータとして渡す
            result = exec_query(query, (work_id,), fetch_all=True)
            if result:
                results.extend(result)
        
        if results:
            return jsonify(results)
        else:
            return jsonify({'error': 'works not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500