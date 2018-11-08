import profile
from collections import OrderedDict
from memory_profiler import profile

class Test:
    @profile
    def group(self, arr):
        """
        Given an array of numbers, your function should return an array of arrays,
        where each subarray contains all the duplicates of a particular number.
        Subarrays should be in the same order as the first occurence of the number they contain
        such as:
        group([3, 2, 6, 2, 1, 3])
        >>> [[3, 3], [2, 2], [6], [1]]
        :param arr:
        :return:
        """
        res = list()
        temp = list()
        if not arr:
            return list()
        else:
            for i in range(len(arr)-1):
                if arr[i] not in temp:
                    temp.append(arr[i])
                    res.append([arr[i]] * arr.count(arr[i]))

            if arr[-1] not in temp:
                res.append([arr[-1]])
            print(res)
            return res

    @profile
    def group_second(self, arr):
        d = OrderedDict()
        for x in arr:
            d.setdefault(x, []).append(x)
        return list(d.values())

import re
s = '{"content"：["akgjajgkajka"]}'
pat = re.compile(r'"content"：\[.*?\]')
res = pat.findall(s)
print(res)




if __name__ == "__main__":
    arrs = [3, 2, 6, 2, 1, 3]
    obj = Test()
    # obj.group(arrs)
    # obj.group_second(arrs)
    # obj.group(arrs)
    # profile.run('obj.group(arrs)')
    # profile.run('obj.group_second(arrs)')
