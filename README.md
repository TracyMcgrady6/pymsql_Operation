# Python3 MySQL 数据库操作
## 什么是 PyMySQL？
PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。
PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。

## PyMySQL 安装
在使用 PyMySQL 之前，我们需要确保 PyMySQL 已安装。
PyMySQL 下载地址：https://github.com/PyMySQL/PyMySQL。
如果还未安装，我们可以使用以下命令安装最新版的 PyMySQL：

```python
pip install PyMySQL
```

## 数据库连接

* 您已经创建了数据库 database_name.
* 在TESTDB数据库中您已经创建了表 EMPLOYEE
* EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
* 连接数据库TESTDB使用的用户名为 "username" ，密码为 "password"。当然可以自己更改

#### 实例：
connect.py

```python
# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='username', passwd='password', db='database_name', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
```
输出结果：

```
Database version : 5.5.20-log
```

## 创建数据库表
#### 实例
create_table.py

```python
# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='username', passwd='password', db='database_name', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
```

## 数据库查询
#### 实例
query.py

```python
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
```

## 数据库插入
#### 实例
insert.py

```python
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
```

## 数据库批量插入
有一个很cooooooooooool的功能就是批量操作executemany，可以进行多行插入
先写sql语句。要注意的是里面的参数，不管什么类型，统一使用%s作为占位符
例如，向user表(username,salt,pwd)插入数据

```python
sql = 'INSERT INTO 表名 VALUES(%s,%s,%s)'
```
对应的param是一个tuple或者list

```python
param = ((username1, salt1, pwd1), (username2, salt2, pwd2), (username3, salt3, pwd3))
```
这样就包含了三条数据，通过executemany插入

```python
n=cursor.executemany(sql,param)
```
#### 实例
insert_batch.py

```python
# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='username', passwd='password', db='database_name', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, AGE, SEX) VALUES (%s,%s,%s)"
# 一个tuple或者list
T = (('xiaoming', 31, 'boy'), ('hong', 22, 'girl'), ('wang', 90, 'man'))

try:
    # 执行sql语句
    cursor.executemany(sql, T)
    # 提交到数据库执行
    db.commit()
except :
    # 如果发生错误则回滚
    db.rollback()
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
```

## 数据库修改更新
#### 实例

```python
# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='username', passwd='password', db='database_name', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % 'M'
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
```

## 数据库删除
#### 实例

```python
# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='username', passwd='password', db='database_name', charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % 20
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
```
