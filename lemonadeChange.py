def lemonadeChange(bills):
    res = []
    for i in bills:
        if i == 5:
            res.append(i)
        elif i == 10:
            res.append(10)
            if res.count(5) > 0:
                res.remove(5)
            else:
                return False
        elif i == 20:
            if res.count(10) > 0 and res.count(5) > 0:
                res.remove(5)
                res.remove(10)
            elif res.count(10) <= 0 and res.count(5) >= 3:
                res.remove(5)
                res.remove(5)
                res.remove(5)
            else:
                return False
    else:
        return True


# a = [5, 5, 10, 10, 20]
a = [5, 5, 5, 10, 5,10,5, 20, 5,20,5,20,10]
print(lemonadeChange(a))
"""
柠檬水找零
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，
也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 
"""