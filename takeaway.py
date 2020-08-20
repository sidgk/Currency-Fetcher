data = "id,name,age,score\n16,jack,NULL,12\n17,Betty,28,11"
#data = "header,header\nANNUl,ANNULLED\nnull,NIL\nNULL,NULL\nnull,null\nNULL,NULL\nxxx,NULL"
def solution(data):
    data = data.split('\n')
    if len(data)>=2:
        header = data[0]
        for i in header.split(','):
            if i == "NULL" or i == "null" or i == "":
                exit(-1)
            else:pass
        data = data[1:]
        for i in data:
            for j in i.split(','):
                if 1 <= len(j) <= 200000:
                    pass
                else:
                    exit(-1)
                if j.isalnum():
                    pass
                else:
                    exit(-1)
                if j == 'NULL':
                    try:data.remove(i)
                    except ValueError:pass
    return header+'\n'+str('\n'.join(data))
    
print(solution(data))