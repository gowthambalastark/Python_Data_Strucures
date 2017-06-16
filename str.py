'''s="aaabbbccc"
g=""
a=[]
b=[]
l=list(s.split(" "))
for i in range(len(l)):
    if i!=(len(l))-1:
        g=g+l[i]+'%20'
    else:
        g=g+l[i]
print(g)
for i in s:
    if i not in a:
        a.append(i)
for i in a:
    b.append(str(i)+str(s.count(i)))
k=''.join(b)
if len(k) != len(s):
   l2=len(s)-len(k)
   for i in range(l2):
       k=k+' '
       s=k
else:
     s=k
print(s)
a=[[int(input()) for i in range(3)] for j in range(3)]
l2=[]
l1=[]
for i in range(3):
    for j in range(3):
        if a[i][j]==0:
            l1.append(i)
            l2.append(j)
            break
for i in range(len(l1)):
    for j in range(3):
         a[l1[i]][j]=0
for i in range(len(l2)):
    for j in range(3):
         a[j][l2[i]]=0
print('\n'.join([''.join(['{:2}'.format(item) for item in row])for row in a]))
def rotate(matrix, degree):
    if abs(degree) not in [0, 90, 180, 270, 360]:
        print("")
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(list(zip(*matrix[::-1])), degree-90)
    else:
        return rotate(list(zip(*matrix[::-1])), degree+90)
l=[0,1,2,3,10]
m=2000
d=90
def fib(n):
        if n==0:
            return '1'    
        elif n==1:
            return '0'
        elif n==2:
            return '1'
        elif n==3:
            return '0'
        elif n==4:
            return '1'
        else:
            for i in range(len(l),n+1):
                l.append(1*l[i-1]+2*l[i-2]+3*l[i-3])
            return '1' if (1*l[n-1]+2*l[n-2]+3*l[n-3])%2==0 else '0'
matrix=[[fib((i*j)**2) for i in range(1,8)]for j in range(1,8)]
ma=[[0 for i in range(m)]for j in range(m)]
for i in range(m):
    for j in range(m):
        try:
            ma[i][j]=matrix[i][j]
        except:
            if i>=7 and j<7:
                ma[i][j]=matrix[(i%7)][j]
            elif j>=7 and i<7:
                ma[i][j]=matrix[i][(j%7)]
            elif i>=7 and j>=7:
                ma[i][j]=matrix[(i%7)][(j%7)]
b=rotate(ma,d)
#print('\n'.join([''.join(['{:2}'.format(item) for item in row])for row in b]))
#print('\n'.join([''.join(['{:2}'.format(item) for item in row])for row in ma]))
c=0
for i in range(m):
    for j in range(m):
        if ma[i][j]!=b[i][j]:
            c+=1
print(c)
T=1
for i in range(1):
    n=3
    nim=list(map(int,input().split()))
    nimsum=nim[0]
    for j in range(1,n):
        nimsum=nim[j]^nimsum
    if nimsum==0:
        print("L")
    else:
        print("W")
from collections import Counter
l=[1,2,3,5,6,7,8,9,1,2,3,4,5,1,2,3]
f,g=list(set(l)),list(set(l))
y=Counter(l)
c=list(y.values())
x=list(y.keys())
print(c,x)
for i in range(len(c)):
    if c[i]==1:
        print(x[i])
for i in g:
    if l.count(i)>1:
       f.remove(i)
print(f)
from collections import Counter
from random import randint
l,l1,l2,d=[],[],[],{}
[l.append(randint(0,10**5)) for i in range(10**5)]
d=Counter(l)
for i,j in sorted(d.items()):
    l1.append(i)
    l2.append(j)
print(d)
print(l1[l2.index(max(l2))],max(l2))
n=int(input())
for i in range(n):
    d,c,l=map(int,input().split())
    if (d+c)*4==l:
        print("yes")
    elif c==d or d>c:
        if d*4==l:
            print("yes")
        else:
            g=[]
            g=list(str(l))
            try:
                k=int(''.join(g[-2]+g[-1]))
            except:
                k=int(g[-1])
            if k%4==0 and l>(d*4):
                print("yes")
            else:
                print("no")
                
    else:
         g=[]
         g=list(str(l))
         try:
             k=int(''.join(g[-2]+g[-1]))
         except:
             k=int(g[-1])
         if k%4==0 and l>=((c-d)*4):
             print("yes")
         else:
             print("no")
a,b,g=11,5,''
s="meet me"
for i in s:
    if ord(i)!=32:
        c=((a*(ord(i)-ord('a'))+b)%26)+(ord('a'))
        g+=chr(c)
    else:
        g+=' '
print(g)
s=''
for i in g:
    if ord(i)!=32:
        c=((-a%26)*(ord(i)-ord('a')-b))%26+ord('a')
        s+=chr(c)
    else:
        s+=' '
print(s)
from collections import Counter,OrderedDict
l=['shobana','banu','banu','bala','bala']
class OderedCounter(Counter,OrderedDict):
    pass
p=OderedCounter(sorted(l)).most_common(1)
print(p)'''
s,g,n='hefg','',''
if s==sorted(s,reverse=True):
    print("Nope")
else:
    for i in range(len(s)-1,0,-1):
        g=s[i:]
        if g==''.join(sorted(g,reverse=True)):
            n=g
            continue
        else:
            break
    n=list(n)
    t=list(s[:len(s)-len(n)])
    c=t[len(t)-1]
    d=min([x for x in n if x>c])
    t[len(t)-1]=d
    n[n.index(d)]=c
    n.sort()
    print(''.join(t+n))
        
    

    

            
    

