
import pymysql


def connect():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='temp', charset='utf8')
    cur = conn.cursor()
    return cur, conn


def create_table():
    cur, conn = connect()
    sql_use = 'use temp;'
    cur.execute(sql_use)

    sql = "create table if not exists test_base4(" \
          "base_id int auto_increment primary key," \
          "base_name varchar(10) not NULL)engine=Innodb charset=utf8"

    cur.execute(sql)
    close_conn(cur, conn)


def drop_database():
    cur, conn = connect()
    sql_drop = 'drop table test_base3;'
    # sql_drop = 'delete from test_base2;'
    cur.execute(sql_drop)
    res = cur.fetchall()
    print(res)
    close_conn(cur, conn)


def insert_data():
    cur, conn = connect()
    sql = 'insert into test_base3(base_id,base_name) VALUES(0, "zhangsan");'
    try:
        cur.execute(sql)
        conn.commit()
        print('执行成功')
        res = cur.fetchall()
        print('insert', res)
    except Exception as e:
        print(e)

    close_conn(cur, conn)


def update_data():
    cur, conn = connect()
    sql = "update test_base3 set base_name='lisi';"
    cur.execute(sql)
    conn.commit()
    res = cur.fetchall()
    print('update', res)
    close_conn(cur, conn)


def select_data():
    cur, conn = connect()
    sql_use = 'use certificate;'
    cur.execute(sql_use)
    # sql = 'select * from marathon_users where id<10;'
    # sql = 'select number from marathon_users where id<10 UNION SELECT names from marathon_users where id<10;'
    # sql = 'select names from marathon_users where id<15 UNION SELECT names from marathon_users_copy where id<15 order by names;'
    # sql = 'select nation from marathon_users where id<15 UNION all SELECT nation from marathon_users_copy where id<15 order by nation;'
    sql = 'select gender,count(*) from marathon_users group by gender;'
    cur.execute(sql)
    conn.commit()
    res = cur.fetchall()
    print('select', res)
    close_conn(cur, conn)


def close_conn(cur, conn):
    cur.close()
    conn.close()



if __name__ == "__main__":
    # drop_database()
    # create_table()
    # insert_data()
    # update_data()
    select_data()