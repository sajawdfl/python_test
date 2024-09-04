# def factorial(num):
#     f = 1
#     for i in range(num):
#         f = num * f
#         num -= 1
#     return f



# def fibonacci(n):
#     a , b = 0 , 1
#     ls = []
#     for i in range(n):
#         a , b = a , a + b
#         a , b = b , a
#         ls.append(b)
#     return ls



# def is_palindrome(num):
#     if str(num) == str(num)[::-1]:
#         return True
#     else:
#         return False


# def is_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
    

# def insertion_sort(list):
#     for i in range(1,len(list)):
#         while list[i] < list[i - 1] and i > 0:
#             list[i - 1] , list[i] = list[i] , list[i - 1]
#             i -= 1
#     return list 



# def roman(character):
#     dic = {'I' : 1 ,
#            'V' : 5 ,
#            'X' : 10 ,
#            'L' : 50 ,
#            'C' : 100 ,
#            'D' : 500 ,
#            'M' : 1000 ,}
#     result = 0
#     temp = 0
#     for i in character[::-1]:
#         if dic[i] < temp:
#             result -= dic[i]
#         else:
#             result += dic[i]
#         temp = dic[i]
#     return result

# print(roman('MCMXCIV'))



# def last_word(string):
#     a = string.split()
#     print(type(len(a[-1])))
# last_word('   fly me   to   the moon  ')



# class Solution(object):
#     def addTwonumbers(self,l1,l2):
#         s1 = ''
#         s2 = ''
#         result_list = []
#         for i in l1[::-1]:
#             s1 += str(i)
#         for j in l2[::-1]:
#             s2 += str(j)
#         result_num = int(s1) + int(s2)
#         for i in str(result_num)[::-1]:
#             result_list.append(int(i))
#         return result_list
# sol = Solution()
# print(sol.addTwonumbers([2,4,3],[5,6,4]))



def add(x , y ):
    return x + y


def subtract( x , y):
    return x - y


def multipy(x , y):
    return x * y 

def division(x , y):
    if y == 0:
        raise ZeroDivisionError('cant devide by zero')
    return x / y
