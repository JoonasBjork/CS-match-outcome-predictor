from queries.sql_creation import inDB


def createTable(conn, query):
    conn.cursor().execute(query)
    conn.commit()


def tableExists(cursor, tableName):
    res = cursor.execute(inDB, [tableName])
    if (len(res.fetchall())) == 0:
        return False
    else:
        return True


def insertIntoTable(cursor, query, data):
    cursor.execute(query, data)
