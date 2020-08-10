class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        sub = ''
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return ans
print(lengthOfLongestSubstring("abcddsacbc"))

'''
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    str_list = []
    max_length = 0
    
    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x)+1:]
            
        str_list.append(x)    
        max_length = max(max_length, len(str_list))
        
    return max_length
    '''