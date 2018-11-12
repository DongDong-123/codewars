class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        lll=list()
        word_list = list()
        num_list = list()

        for elem in logs:
            # print(elem)
            log_words = elem.split(' ')
            # print(log_words)
            temp = log_words[1:]
            # print(temp)
            # for strs in temp:
            if isinstance(self.func(temp), str):
                temp.sort()
                word_list.append(temp)
            else:
                num_list.append(temp)

        print(word_list)
        print(num_list)

    def func(self,temp):
        bas = 0
        for i in temp:
            if isinstance(eval(i), str):
                bas += 1

        if bas == len(temp):

            return True
        else:
            return False



            # print(temp)
            # temp.insert(0, log_words[0])
            # keys = log_words[0]
            # dict_temp = {keys: temp}
            # print(dict_temp)
            # lll.append(dict_temp)
            # print(temp)
            # res = ' '.join(temp)
            # print(res)
            # lll.append(res)

        # tt = lll.sort(key=lambda x:x[1:])
        # print(lll)
        # for ele in s:



if __name__ == "__main__":
    aims = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    s = "aba"
    res = Solution()
    res.reorderLogFiles(aims)
    # res.reorderLogFiles(s)
    result = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]

    c = ['9 2 3 1', "act car", '4 7','off key dog']