class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        from collections import Counter
        c_list = A.split() + B.split()
        c_count = dict(Counter(c_list))

        return [i for i in c_count.keys() if c_count[i] == 1]


A = "this apple is sweet"
B = "this apple is sour"
a = Solution()
print(a.uncommonFromSentences(A,B))

"""
class Solution:
    def uncommonFromSentences(self, A, B):
        
        res = collections.defaultdict(int)
        ret = []
        for i in A.split():
            res[i] += 1
        for i in B.split():
            res[i] += 1
        for key, value in res.items():
            if value == 1:
                ret.append(key)
        return ret
        
"""