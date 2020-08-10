class Solution:
    def kidWithCandies(candies, extraCandies):
        #l = len(candies)
        ans = []
        maxcandy = max(candies)
        for i in range(len(candies)):
            if i + extraCandies > maxcandy:
                ans.append(True)
            else:
                ans.append(False)
        return ans

candies = [2,3,5,1,3]
extraCandies = 3
print(list(kidWithCandies(candies,extraCandies)))

'''
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        l=len(candies)
        ans=[]
        for i in range(l):
            if candies[i]+extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans'''