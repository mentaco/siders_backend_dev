from typing import Optional, Union, List, Tuple, Dict
from psycopg2 import extras
from ..database import db_pool

'''
データベースにクエリを送る関数
query: SQL文
params: SQL文に含めるパラメータ(タプル or 辞書)
fetch_all: クエリの結果を返すかどうか
'''
def exec_query(
        query: str,
        params: Optional[Union[Tuple, Dict]] = None,
        fetch_all: bool = True) ->  Optional[List[Dict]]:
    conn = db_pool.getconn()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    try:
        cur.execute(query, params)

        if fetch_all:
            result = cur.fetchall()
        else:
            result = None

        conn.commit()
        return result

    except Exception as e:
        conn.rollback()
        print(e)
        raise e

    finally:
        cur.close()
        db_pool.putconn(conn)
