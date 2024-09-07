# def is_prime(m):
#     for i in range(2,m):
#         if m % i ==0:
#             return False
#     return True

# def prime(n):
#     ls = []
#     for i in range(2,n):
#         total = 0
#         for j in range(2,i):
#             if i % j ==0:
#                 total+=1
#         if total < 1:
#             ls.append(i)
#     return ls
# print(prime(21)) 



# def prime(n):
#     ls = []
#     for i in range(2,n):
#         # print(i)
#         for j in range(2,i):
#             # print(i,j)
#             if i % j ==0:
                
#                 # print(i,j)
#                 break
#         else:    
#             ls.append(i)
#     return ls                
    
# print(prime(21))


# def prime(n):
#     a = list(range(2,n))
#     ls = []
#     prime = []
#     for i in range(2,n):
#         for j in range(2,i):
#             if i % j ==0:
#                 # print(i)
#                 ls.append(i)
#     ls = set(ls)
#     ls = list(ls)
#     # print(a)
#     for n in a:
#         if n not in ls:
#             prime.append(n)
#     return prime        
# print(prime(21))



# def prime(n):
#     ls = []
#     for i in range(2,n):
#         total = 0
#         for j in range(2,i):
#             if i % j ==0:
#                 total +=1
#         if total < 1:
#             ls.append(i)
#             print(i)
    
# prime(24)



# def fib(n):
#     a = (n**2*5-4)
#     b = (n**2*5+4)
#     a2 = (int(a ** (1/2)))
#     b2 = (int(b ** (1/2)))
#     print(a,b)
#     print('-------------------')
#     print(a2,b2)
#     print('-------------------')
#     if (a2 ** 2 == a) or (b2 ** 2 ==b):
#         print(f'{n} is a fibonacci number')
#     else:
#         print(f'{n} is not a fibonacci number')
    
# fib(41)



# def find_min(list):
#     min = list[0]
#     for i in range(len(list)):
#         if list[i] < min:
#             min = list[i]
#     return min


# def sort(list):
#     for i  in range(len(list)) :
#         for j in range(i,len(list)):
#             if  list[j]<list[i]:
#                 temp=list[i]
#                 list[i]=list[j]
#                 list[j]=temp
#     print(list)                            
# sort([4,2,5,3,1])


# def insertion(list):
#     for i in range(1,len(list)):
#         current_value = list.pop(i)
#         for j in range( i-1, -1 ,-1):
#             if list[j] > current_value:
#                 print(i,j)
#                 i = j
#         list.insert(i ,current_value)
#     print(list)
    
# insertion([2,6,5,3,7,4,1])






# def kart_melli(num):
#     ls = []
#     n = []
#     for i in num:
#         ls.append(int(i))
#     k=10  
#     for i in range(len(ls)):
#         n.append(ls[i] * k)
#         k-=1
#     n_sum = sum(n)
#     if n_sum % 11 ==1:
#         print(str(num)+'1')
#     elif n_sum % 11 > 1:
#         frz = 11 - (n_sum % 11)
#         frz_str = str(frz)
#         print(str(num) +frz_str )
        
# print(kart_melli('002292696'))




# def kart_melli(char):
#     n = []
#     k=10
#     for i in char:
#         n.append(int(i) * k)
#         k-=1
#     mod = sum(n)%11
#     if mod ==1:
#         checkdigit=mod
#     elif mod > 1:
#         checkdigit=11 - mod
        
#     print(char+""+str(checkdigit))  
        
# print(kart_melli('002292696'))


# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

    
    
# def is_palindrome(num):
#     first_num = num
#     temp = 0
#     mod = 1
#     while num != 0:
#         mod = num % 10
#         temp = (temp * 10) + mod
#         num = num // 10
#     return first_num == temp



# def palindrome(num):
#     i = 0

#     while True :
#         i+=1
#         if is_palindrome(num-i):
#             return num-i
#         elif is_palindrome(num+i):
#             return num+i


# def roman(character):
#     dic= {'I' : 1 ,
#         'V' : 5,
#         'X' : 10,
#         'L' : 50,
#         'C' : 100,
#         'D' : 500,
#         'M' : 1000
#         }
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



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    
# class Solution:
#     def addTwonumbers(self,l1,l2):
#         print(l1,l2)

    
#     def add(self,l1,l2):
#         head=None
#         n=l1
#         while(n!=None):
#             x=ListNode(n.val)
#             x.next=head
#             head=x;  
#             n=n.next    
#         n=l2
#         while(n!=None):
#             x=ListNode(n.val)
#             x.next=head
#             head=x;  
#             n=n.next 
#         return head 
#     def check(self,l3):
#         n=l3
#         while(n!=None):
#             print(n.val)
#             n=n.next

# firstlist=ListNode(2, ListNode(4,ListNode(3)))
# secondList=ListNode(5,ListNode(6,ListNode(4)))

# solmol = Solution()
# # solmol.check(firstlist,secondList)
# l3=solmol.add(firstlist,secondList)
# solmol.check(l3)


# def syntax_check(string):
#     open_list = ["(" , "[" , "{"]
#     close_list = [")" , "]" , "}"]
#     stack = []
#     for i,j in enumerate(string):
#         if j in open_list:
#             pos1 = open_list.index(j)
#             stack.append(j)
#         elif j in close_list:
#             pos2 = close_list.index(j)
#             stack.pop()
#     if len(stack) == 0:
#         return True    
#     return False    
        

# print(syntax_check('([])'))






































































































































































































































































































































































































































































































































































































































































































































