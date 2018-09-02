class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        a_list = []
        b_list = []

        for i in range(len(dislikes)):
            a_list.append(dislikes[i][0])
            b_list.append(dislikes[i][1])
        for i in a_list:
            if b_list[i]:
                return False
        for i in b_list:
            if a_list[i]:
                return False
        return True

    # res_list = []
    # def circle(self, N):
    #     for i in range(1, N+1):
    #         for v in range(i+1, N+1):
    #             per = [i, v]
    #             print(per)
    #             if per in dislikes:
    #                 pass
    #             else:
    #                 # return True
    #                 res_list.append(per)
    #
    #     if len(res_list) >= N // 2:
    #         return True
    #     else:
    #         return False
            # yield per


    # def Dislike(self, N, dislikes):
    #     n = 0
    #     # while n < 50:
    #     try:
    #         res = self.circle(N)
    #         print(list(res))
    #         n += 1
    #     except:
    #         pass

# dislikes =[[1,2],[2,3],[3,4],[4,5],[1,5]]
# dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# dislikes = [[1,2],[1,3],[2,3]]
dislikes = [[1,2],[1,3],[2,4]]
a = Solution()
print(a.possibleBipartition(4,dislikes))

"""
求出所有的分组可能，
"""


class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if K == 1:
            return N

        f = [collections.defaultdict(int) for i in range(N + 5)]
        for i in range(1, N + 5):
            for j in range(K):
                f[i][j] = f[i - 1][j - 1] + f[i - 1][j] + 1
            if max(f[i].values()) >= N:
                return i


class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        edges = [[] for i in range(N)]
        for pair in dislikes:
            edges[pair[0] - 1].append(pair[1] - 1)
            edges[pair[1] - 1].append(pair[0] - 1)

        team = [-1 for i in range(N)]
        for i, p in enumerate(team):
            if p == -1:
                team[i] = 0
                q = collections.deque()
                q.append(i)
                while len(q):
                    pre = q.popleft()
                    for j in edges[pre]:
                        if team[j] == -1:
                            team[j] = 1 - team[pre]
                            q.append(j)
                        elif team[j] == team[pre]:
                            return False
        return True


class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ret = [[r0, c0]]
        step = 0
        while len(ret) < R * C:
            step += 1
            for i in range(step):
                c0 += 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    ret.append([r0, c0])
            for i in range(step):
                r0 += 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    ret.append([r0, c0])

            step += 1
            for i in range(step):
                c0 -= 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    ret.append([r0, c0])
            for i in range(step):
                r0 -= 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    ret.append([r0, c0])
        return ret

from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = Counter(A.split(' '))
        b = Counter(B.split(' '))
        f = lambda c1, c2: [k for k, v in c1.iteritems() if v == 1 and k not in c2]
        return f(a, b) + f(b, a)


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        def path(r, c, n):
            yield r, c
            for d in xrange(1, n + 1):
                for i in xrange(1, 2 * d + 1): yield r - d + i, c + d
                for i in xrange(1, 2 * d + 1): yield r + d, c + d - i
                for i in xrange(1, 2 * d + 1): yield r + d - i, c - d
                for i in xrange(1, 2 * d + 1): yield r - d, c - d + i

        return [(i, j) for i, j in path(r0, c0, max(R, C)) if 0 <= i < R and 0 <= j < C]


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        c = [None for _ in xrange(N+1)]
        d = [set() for _ in xrange(N+1)]
        for i, j in dislikes:
            d[i].add(j)
            d[j].add(i)
        def visit(s):
            if c[s] is not None: return True
            v = 0
            q = set([s])
            while q:
                nq = set()
                for i in q:
                    if c[i] is not None and c[i] != v: return False
                    c[i] = v
                    for j in d[i]:
                        d[j].remove(i)
                        nq.add(j)
                    d[i].clear()
                q = nq
                v = 1 - v
            return True
        return all(visit(i) for i in xrange(N+1))


class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if K >= 13:
            r = 0
            while N:
                N //= 2
                r += 1
            return r
        r = range(N+1)
        s = [0]*(N+1)
        for _ in xrange(K-1):
            for n in xrange(1, N+1):
                a = 1
                b = n
                while a + 1 < b:
                    c = (a + b) // 2
                    if r[c-1] < s[n-c]: a = c
                    else: b = c
                s[n] = 1+min(max(r[a-1], s[n-a]), max(r[b-1], s[n-b]))
            r, s = s, r
        return r[-1]