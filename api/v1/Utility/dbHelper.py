import sqlite3 as db
from logger import logger as logger

db_file = "systemdb"


def execute_sql(sql: str):
    try:
        conn = db.connect(db_file)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except:
        logger.warning(f"执行sql失败！[{sql}]")
    finally:
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result


def exist_table(table_name: str):
    conn = db.connect(db_file)
    cur = conn.cursor()
    cur.execute(f"select count(1) from sqlite_master WHERE type=\"table\" AND name = \"{table_name}\"")
    cur.close()
    conn.close()
    return True



if __name__ == '__main__':
    execute_sql("create table USER(NAME char(12),KEY char(16),GUID char)")
