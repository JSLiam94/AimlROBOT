
import sqlite3
import datetime
import sqlite3
              
              

              
conn = sqlite3.connect('LDT.db')
cursor = conn.cursor()

             
sql = '''select * from LDT'''

              
              

     #执行语句
results = cursor.execute(sql)

              # 遍历打印输出
LIUYAN= results.fetchall()

for I in LIUYAN:
        print(I)
