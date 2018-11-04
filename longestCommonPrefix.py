class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        duck = []
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""
        else:
            min_str = min(strs)
            strs.remove(min_str)
            if min_str:
                for m in strs:
                    nums = 0
                    for i, v in enumerate(m[:len(min_str)]):
                        if min_str[i] == v:
                            nums += 1
                        else:
                            break

                    duck.append(nums)
            else:
                return ''

            res = min(duck)
            if res == 0:
                return ''
            else:
                return min_str[:res]


if __name__ == "__main__":
    # str_list = ["aba", "c", "b", "a", "ab"]
    str_list = ["flower", "flow", "flight"]
    # str_list = ["dog", "racecar", "car"]
    temp = Solution()
    print(temp.longestCommonPrefix(str_list))
    """
    最长公共前缀，注意空值，需要对值进行判断
    """
