def insertion_sort(list):
    for i in range(1,len(list)):
        while list[i] < list[i - 1] and i > 0:
            list[i - 1] , list[i] = list[i] , list[i - 1]
            i -= 1
    return list 
