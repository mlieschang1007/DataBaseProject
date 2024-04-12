from flask import Flask , render_template
from connectDataBase import connect_database,DatabaseConnectionError


#創建 Flask 應用程式物件
app = Flask(__name__)




try:
    connection,cursor = connect_database()
    db_connected = True
except DatabaseConnectionError:
    db_connected = False


# 額外的路由，用來檢查資料庫連接狀態
@app.route('/check_db_connection')
def check_db_connection():
    if db_connected:
        return '資料庫連接成功!'
    else:
        return '資料庫連接失敗!'

cursor.close()
connection.close()
#是flask 用於定義路由，當用戶訪問特定的url時應該執行的程式碼，此裝飾告訴Flask應用程式要將下面定義的函示與特定的URL路徑關聯
@app.route('/')
def index():
    return '歡迎使用選課系統!'

# 啟動 Flask 應用程式
#當這個程式檔案被直接執行時，也就是當它是主程式時（而不是被其他程式模組引入時）。
#此時，會執行 app.run(debug=True)，這個函式會啟動 Flask 應用程式，並開啟偵錯模式，以便在開發過程中進行偵錯。
if __name__ == '__main__':
    app.run(debug=True)



