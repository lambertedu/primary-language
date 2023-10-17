def expo_func(base_num, index_num):
    resault = 1
    for index in range(index_num):
        resault = resault * base_num
    return resault


print(expo_func(5, 2))
