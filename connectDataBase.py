import mysql.connector

# 建立資料庫連線
connection = mysql.connector.connect(
    host='localhost',
    port='3307',  # 根據你的設定修改埠號
    user='root',
    password='',  # 根據你的資料庫密碼填寫
    database='course'
)

# 建立游標物件
cursor = connection.cursor()

# 執行 SQL 查詢
cursor.execute('SHOW TABLES;')

# 提取查詢結果
tables = cursor.fetchall()

# 顯示查詢結果
for table in tables:
    print(table[0])

# 關閉游標和資料庫連線
cursor.close()
connection.close()
