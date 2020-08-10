'''from typing import List, Tuple

def twosum_indices_linear(nums: List[int], target: int) -> Tuple[int, int]:
    numtoindexmap = {}
    for num1_index, num1 in enumerate(nums):
        num2 = target - num1
        try:
            num2_index = numtoindexmap[num2]
        except KeyError:
            numtoindexmap[num1] = num1_index  
            # Note: Use `numtoindexmap.setdefault(num1, num1_index)` instead for lowest num1_index.
        else:
            return tuple(sorted([num1_index, num2_index]))

print(twosum_indices_linear([2,5,4,7, 11, 15], 9))'''


from typing import List, Tuple
def twosum_indices_linear(nums: List[int], target: int) -> Tuple[int, int]:
    traversed = {}
    for i, v in enumerate(nums):
        diff = target - v
        if diff in traversed:
            return [traversed[diff], i]
        if v not in traversed:
            traversed[v] = i
    return []

nums = [2,7,11,8]
target = 9
print(twosum_indices_linear([2,5,4,7, 11, 15], 9))
print(twosum_indices_linear(nums,target))