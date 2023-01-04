import sqlite3

def initializeDB(dbname):
    conn = sqlite3.connect(dbname)
    return conn

def createCursor(conn):
    try:
        cursor = conn.cursor()
        return cursor
    except:
        print('Not a valid connection')

sqlConnection = initializeDB('bankDb2.db')
cursor = createCursor(sqlConnection)
# query = """CREATE TABLE User(
#     Name text,
#     NIN text primary key,
#     balance integer
# )"""
# cursor.execute(query)
# sqlConnection.commit()
# print('Table Created')

def insertValues(name,nin,balance):
    query2 = f"INSERT INTO User VALUES('{name}','{nin}',{balance})"
    cursor.execute(query2)
    print('User added')
    sqlConnection.commit()

query3 = "SELECT * FROM User"
cursor.execute(query3)
result = cursor.fetchall()
print(result)
