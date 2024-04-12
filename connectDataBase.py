import mysql.connector
class DatabaseConnectionError(Exception):
    pass



# 用函數建立資料庫連線
def connect_database():
    connection = mysql.connector.connect(
        host='localhost',
        port='3307',  # 根據你的設定修改埠號
        user='root',
        password='',  # 根據你的資料庫密碼填寫
        database='course'
        )


    # 建立游標物件
    cursor = connection.cursor()
    #返回游標物件
    return connection,cursor

# 執行 SQL 查詢
#cursor.execute('SHOW TABLES;')

# 提取查詢結果
#tables = cursor.fetchall()

# 顯示查詢結果
#print("目前有的table:")
#for table in tables:
#print(table[0])


#顯示 table 架構
#cursor.execute('DESCRIBE course_details')
#columns = cursor.fetchall()
#print("course_details table 架構:")
#for column in columns:
    #print(column)

#cursor.execute('DESCRIBE students')
#columns = cursor.fetchall()
#print("students table 架構:")
#for column in columns:
#print(column)

#cursor.execute('SELECT * FROM course_details')

# 提取查詢結果
#details = cursor.fetchall()

# 顯示 course_details table 的內容
#print("course_details table 內容:")
#for detail in details:
    #print(detail)


# 關閉游標和資料庫連線
#cursor.close()
#connection.close()
