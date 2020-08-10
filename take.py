def solution(n):
   if(n>=1 and n<=100):
       result =[]
       for i in range(1,n//2+1):
           result.append(i)
           result.append(-i)
       if n%2!=0:
           result.append(0)
       print(result)
       return result
   else:
       print("N should bebetween 1 and 100")

solution(3)
solution(5)