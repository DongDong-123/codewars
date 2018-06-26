def declare_winner(fighter1,fighter2,first_attacker):
    a,b,c,d = fighter1[1],fighter2[1],fighter1[2],fighter2[2]
    if first_attacker == fighter2[0]:
        #while a >=0 and b >= 0 :
        while True:
            b -= c
            a -= d
            if b <= 0:
                winer = fighter1[0]
                return winer
            if a <= 0:
                winer = fighter2[0]
                return winer
        return winer

    else:
        #while a >=0 and b >= 0:
        while True:
            a -= d
            b -= c
            if a <= 0:
                winer = fighter2[0]
                return winer
            if b <= 0:
                winer = fighter1[0]
                return winer
        return winer
    return winer

fighter1 = ('lew',10,2)
fighter2 = ('harry',5,4)
first_attacker = 'lew'
winers = declare_winner(fighter1,fighter2,first_attacker)
print(winers)