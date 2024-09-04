def roman(character):
    dic = {'I' : 1 ,
           'V' : 5 ,
           'X' : 10 ,
           'L' : 50 ,
           'C' : 100 ,
           'D' : 500 ,
           'M' : 1000 ,}
    result = 0
    temp = 0
    for i in character[::-1]:
        if dic[i] < temp:
            result -= dic[i]
        else:
            result += dic[i]
        temp = dic[i]
    return result