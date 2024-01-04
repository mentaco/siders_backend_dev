from psycopg2 import pool
from .db_info import *

db_pool = pool.SimpleConnectionPool(
        minconn=1,
        maxconn=15,
        host=HOST,
        port=PORT,
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
)
