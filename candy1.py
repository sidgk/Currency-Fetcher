#https://medium.com/@donic0211/leetcode-1431-kids-with-the-greatest-number-of-candies-150a26aa8274

def kidWithCandies(candies, extraCandies):
        #l = len(candies)
        ans = []
        maxcandy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxcandy:
                ans.append(True)
            else:
                ans.append(False)
        return ans
candies = [2,3,5,1,3]
extraCandies = 3
print(list(kidWithCandies(candies,extraCandies)))