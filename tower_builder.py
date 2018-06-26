def tower_builder(n_floors):
    # 方法一
    # list_res = []
    # for i in range(1, 2*n_floors, 2):
    #     #temp = (i+1)//2
    #     list_res.append((n_floors-(i+1)//2)*" " + i * "*"+ (n_floors-(i+1)//2)*" ")
    # return list_res
    # 方法二
    #return [(n_floors-(i+1)//2)*" " + i * "*"+ (n_floors-(i+1)//2)*" " for i in range(1, 2*n_floors, 2)]
    # 方法三
    return [("*"*(2*i-1)).center(2*n_floors -1) for i in range(1, n_floors+1)]

print(tower_builder(3))