#encode:utf-8
import  MySQLdb

def conn_db(sql):
    conn = MySQLdb.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='sALLY0921',
        db='caseResult',
        charset='utf8'
    )
    cur=conn.cursor()
    cur.execute(sql)
    return cur.fetchone()
    # current = str(cur.fetchone())
    # st = current.__str__()
    # print(st.decode('unicode-escape'))

def search_one(sql):
    conn = conn_db()
    with conn as co:
        cur = co.cursor()
        return cur.execute(sql)

if __name__ == "__main__":
    search_one('select * from expectData')