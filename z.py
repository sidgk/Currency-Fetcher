def solution(s):
    if  0 <= len(s) <= 250000 and all(c in "ABCD" for c in s):
        for i in range(0, len(s)):
            if 'CD'or 'DC' in s:
                s = s.replace('CD','')
            if 'DC' in s:
                s = s.replace('DC','')
            if 'AB' in s:
                s = s.replace('AB','')  
            if 'BA' in s:
                s = s.replace('BA','')
        return(s)
print(solution("CBACDE"))
#print(solution("CABADB"))
# print(solution("ACBDACBD"))