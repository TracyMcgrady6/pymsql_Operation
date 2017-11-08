# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='username', passwd='password', db='database_name', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL两种插入格式
sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000)"
sql2 = "INSERT INTO EMPLOYEE(FIRST_NAME, AGE, SEX) VALUES (%s,%s,%s)" % ('Mac', 20, 'boy')

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
