from queries.sql_creation import in_db


def create_table(conn, query):
    conn.cursor().execute(query)
    conn.commit()


def table_exists(cursor, tableName):
    res = cursor.execute(in_db, [tableName])
    if (len(res.fetchall())) == 0:
        return False
    else:
        return True


def insert_into_table(cursor, query, data):
    cursor.execute(query, data)
