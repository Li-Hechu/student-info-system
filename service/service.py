import pymysql

userName = ''


def open():
    db = pymysql.connect(host='localhost', user='root', password='lhy20160922', database='db_student')
    return db


def exec(sql, values):
    db = open()
    cursor = db.cursor()
    try:
        cursor.execute(sql, values)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()


def query(sql, *keys):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def query1(sql):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
