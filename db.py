import pymysql
'''
前提条件：
1、下载MySQL
2、在数据库中建一个名称为MONITORDB的DB
3、执行程序
如果不先建立DB则会报错
'''
class DBStorage(object):
    # 打开数据库连接
    def PreConnect(self):
        db = pymysql.connect(
            host="localhost",
            port=3306,
            user="",
            passwd="",
            db="MONITDB"
        )
        # 使用cursor()方法创建一个游标对象cursor
        cursor = db.cursor()
        return db,cursor

    def CloseConnect(self,sql):
        cursor = self.PreConnect()
        cursor[0].execute(sql)
        cursor[1].close()

     #插入数据
    def InsertInfo(self):
        insertcursor = self.PreConnect()
        #使用execute()方法执行SQL,如果表存在则删除
        insertcursor.execute("DROP TABLE IF EXISTS ARCHINFO")

        #使用预处理语句创建表
        sql = """CREATE TABLE ARCHINFO(
                SYS_TYPE CHAR(30) NOT NULL,
                SYS_BIT INT
                )"""

        self.CloseConnect(sql)

    #查询数据
    def QueryInfo(self):
        querycursor = self.PreConnect()
        #构造查询语句
        sql = "SELECT * FROM ARCHINFO WHERE SYS_TYPE == str("Windows")"
        querycursor[0].execute(sql)
        querycursor[1].close()
