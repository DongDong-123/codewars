class Solution:
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    n = 3
    res = Solution()
    print(res.generateParenthesis(n))


'url', 'title', 'date', 'day', 'who', 'text', 'image'