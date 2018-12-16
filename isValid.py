dicts = {'(':')','{':'}','[':']'}
s = "()[]{}"
r = "([)]"
s_len = len(s)
start = 0
end = 1

for i in range(s_len):
    if dict.get(s[start]) == s[end]:
        start += 2
        end += 2
    else:
        # start +=1
        end += 1
