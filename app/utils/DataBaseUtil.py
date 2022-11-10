import pymysql




class DatabaseUtil(object):
    # def __init__(self):
    #     pass

    # @staticmethod
    def __init__(self, host, user, password, database, port):
        db = pymysql.connect(host=host, user=user, password=password, database=database, port=int(port))
        self.cursor = db.cursor()

    @staticmethod
    def execute_sql(cursor, sql):
        cursor.execute(sql)
        result_list = []
        for every in cursor.fetchall():
            result_list.append(every)
        return result_list

