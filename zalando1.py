pairs = [(4, 11), (8, 8), (5, 7), (11, 3)]
sorted_by_smallest = sorted(pairs, key=lambda items: min(items))


circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1,7)))



multiples = [i for i in range(30) if i % 3 == 0]
squared = [x**2 for x in range(10)]
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
{v: k for k, v in some_dict.items()}
name = ['raj','rajesh','john']
marks = [83,85,96]
record2 = dict()
for i,j in list(zip(name,marks)):
    record2.update({i: j})
or
record3 = {i:j for i,j in zip(name,marks)}
mydict = {'a':1,'b':2,'c':3,'d':4}
record4 = {i:j**2 for i,j in mydict.items()}









def solution(s):
    a = len(s)
    f = 0
    i = 0 

    while f ==0:
        while (i<a-2):
            if(s[i]=='A' and s[i+1]=='B'):
                s = s.replace('AB', '')
                i=0
            else:
                if(s[i]=='B' and s[i+1]=='A'):
                    s = s.replace('BA', '')
                    i=0
                else:
                    if (s[i]=='C' and s[i+1]=='D'):
                        s = s.replace('CB', '')
                        i=0
                    else:
                        if(s[i]=='D' and s[i+1]=='C'):
                            s = s.replace('DC', '')
                            i=0
                        else:
                            f = 1
                            f = i+1
            a=len(s)
    return(s)

solution("CBACD")
solution("CABADB")
solution("ACBDACBD")