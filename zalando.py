class SumZero:
   def MakeSumZero(self,n):
       result =[]
       for i in range(1,n//2+1):
           result.append(i)
           result.append(-i)
       if n%2!=0:
           result.append(0)
       return result

sumzero1 = SumZero()
print(sumzero1.MakeSumZero(6))


'''n = int(input ("Enter the Number : n"))
if(n>=1 and n<=100):
   print("came here")
   print(n)
   sumZero=SumZero()
   print(sumZero.MakeSumZero(n))
else:
   print("Please enter the number beteen 1 to 100")'''