import pymysql


def getConnect():
    conn = pymysql.connect(host='localhost', port=3306, db='team01',
                           user='manager', password='1234', charset='utf8')

    return conn
