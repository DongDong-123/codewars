import pymysql
from jin_du_tiao import progress_bar

# import time
# from functools import wraps
# import random
#
#
# def fn_timer(function):
#     @wraps(function)
#     def function_timer(*args, **kwargs):
#         t0 = time.time()
#         result = function(*args, **kwargs)
#         t1 = time.time()
#         print("Total time running %s: %s seconds" %
#               (function.func_name, str(t1 - t0))
#               )
#         return result
#
#     return function_timer
#
#
# @fn_timer
# def random_sort(n):
#     return sorted([random.random() for i in range(n)])
#
#
# if __name__ == "__main__":
#     random_sort(2000000)

import time

def timeit(func):

    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print('used:', end - start)

    return wrapper

@timeit
def foo():
    print('in foo()')



@timeit
def main():
    """
    copy MySQL数据库内的数据，打印进度条
    :return:
    """

    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='fund_info', charset='utf8')
    cur = conn.cursor()
    sql_count = 'select count(id) from fund_value;'
    cur.execute(sql_count)
    conn.commit()
    num_total = cur.fetchone()[0]
    # print('num_total', num_total)
    num = 0
    while num < num_total:
        progress_bar(num, num_total)
        num += 1
        sql = 'select * from fund_value where id={};'.format(num)
        # print(sql)
        cur.execute(sql)
        result = cur.fetchone()

        res_per_day = result[3]
        res_sum = result[4]

        # print(result[0], result[1],type(result[1]), result[2],type(result[2]), result[3],type(result[3]), result[4])
        # cur = conn.cursor()

        new_sql = 'insert into fund_value_copy(id, fund_id_fu, value_date, value_per_date, value_sum) values("{}", "{}", "{}", "{}", "{}");'.format(result[0], result[1], result[2], res_per_day, res_sum)
        # print(new_sql)
        cur.execute(new_sql)
        conn.commit()

        # print(result, type(result))

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
