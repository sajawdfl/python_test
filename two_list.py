class Solution(object):
    def addTwonumbers(self,l1,l2):
        s1 = ''
        s2 = ''
        result_list = []
        for i in l1[::-1]:
            s1 += str(i)
        for j in l2[::-1]:
            s2 += str(j)
        result_num = int(s1) + int(s2)
        for i in str(result_num)[::-1]:
            result_list.append(int(i))
        return result_list
sol = Solution()
# print(sol.addTwonumbers([2,4,3],[5,6,4]))