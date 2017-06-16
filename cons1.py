l=list(bin(int(input()))[2:])
max,d=0,0
for i in l:
    #print(i,end='')
    if i=='0':
        if d>max:
            max=d 
            d=0
    elif i=='1':
        d+=1
if d>max:
    max=d
print(max)
