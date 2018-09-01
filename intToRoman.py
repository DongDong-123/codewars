class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.num_length = len(str(num))
        num_list = list(map(int, str(num)))
        num_single = [num_list[i] * 10 ** (self.num_length - i - 1) for i in range(self.num_length)]
        print(num_single)


    def ToRoman(self, number):
        # if self.num_length >= 4:
        if number >= 1000:
            return  number / 1000




# a = Solution()
# print(a.intToRoman(1994))
# import collections
# a = [1, 2, 3, 4, 5, 3]
# b = collections.deque(a, maxlen=10)
# print(type(b))
# # b.rotate(2)
# print(b)
# c = b.count(3)
# print(c)
# print(len(a))
# c = [6,7,8,9,0]
# b.extendleft(c)
# print(b)
# d = [1, 3, 4]
# d.extend(c)
# print(d)
#
# e = b[2]
# print('e', e)
# with open(str(collections.__file__), "r") as f:
#     print(f.read())

# import os
# os.makedirs('D:\\Users\\Dong\\Desktop\\funds')
#
# a = os.stat('D:\\Users\\Dong\\Desktop\\funds')
# print(a)
import pymysql

conn = pymysql.connect(host='160.11.123.130', user='root', password='111',db='test')
cur = conn.cursor()
sql = 'insert into table(id,title) values(1,"标题");'
cur.execute(sql)
conn.commit()

sql2 = 'select id,url from v_url'