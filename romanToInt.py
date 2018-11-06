class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_list = [1000, 500, 100, 50, 10, 5, 1]
        roman_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        roman_dict = dict(zip(roman_list, num_list))

        num = 0

        for i in range(len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                num -= roman_dict[s[i]]
            else:
                num += roman_dict[s[i]]

        num += roman_dict[s[-1]]
        return num


if __name__ == "__main__":
    res = Solution()
    roman = "IV"
    print(res.romanToInt(roman))