# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='username', passwd='password', db='database_name', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql1 = "SELECT * FROM EMPLOYEE WHERE NAME = 'xiaoming'"
# SQL 查询语句
sql2 = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % 1000

try:
    # 执行SQL语句
    cursor.execute(sql1)
    # results是个元组对象
    results = cursor.fetchone()
    # 先判断是否为空
    if results is None:
        print("查询为空")
    else:
        print(results)

    # 执行SQL语句
    cursor.execute(sql2)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
