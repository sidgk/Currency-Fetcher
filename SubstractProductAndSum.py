'''def subtract_product_and_sum(n):
    str_n = str(n)
    product_of_digits = 1
    sum_of_digits = 0
    for number in str_n:
        int_n = int(float(number))
        product_of_digits *= int_n
        sum_of_digits += int_n
    diff = product_of_digits - sum_of_digits
    return diff
'''

class Solution(object):
    def subtractProductAndSum(self, n):
        from functools import reduce
        from operator import mul
        digits = [int(x) for x in str(n)]
        return reduce(mul, digits) - sum(digits)
s = Solution()
print (s.subtractProductAndSum(42))