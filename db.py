import pymysql
'''
前提条件：
1、下载MySQL
2、在数据库中建一个名称为MONITORDB的DB
3、执行程序
如果不先建立DB则会报错
'''
class DBStorage(object):

    def InsertInfo(self):
        #打开数据库连接
        db = pymysql.connect(
            host="localhost",
            port=3306,
            user="",
            passwd="",
            db="MONITORDB")
        #使用cursor()方法创建一个游标对象cursor
        cursor = db.cursor()
        #使用execute()方法执行SQL,如果表存在则删除
        cursor.execute("DROP TABLE IF EXISTS ARCHINFO")

        #使用预处理语句创建表
        sql = """CREATE TABLE ARCHINFO(
                SYS_TYPE CHAR(30) NOT NULL,
                SYS_BIT INT
                )"""

        cursor.execute(sql)
        db.close()