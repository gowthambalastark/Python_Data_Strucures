import math,random
def prime():
    l=[]
    for i in range(1000,10000):
        f=1
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                f=0
                break
        if f:
            l.append(i)
    return l
def modexp( base, exp, modulus ):
    return pow(base, exp, modulus)
def primitive_root( p ):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p-1) // p1
    #test random g's until one is found that is a primitive root mod p
    while( 1 ):
        g = random.randint( 2, p-1 )
        #g is a primitive root if for all prime factors of p-1, p[i]
        #g^((p-1)/p[i]) (mod p) is not congruent to 1
        if not (modexp( g, (p-1)//p1, p ) == 1):
            if not modexp( g, (p-1)//p2, p ) == 1:
                return g

def encrypt(p,r,t2):
    e =(t2 ** r % p)
    #print("Encrypted Text is",e)
    return e
def decrypt(p,s,t1):
    d = t1 ** s % p
    i = pow(d,p-2,p)
    return (i)

z=input("Enter Message:")
z=list(z)
z=[ord(i) for i in z]
n=int(input("Enter Number Of Rounds:"))
k=prime()
p=k[random.randint(0,len(k)-1)]
l1,l2,r,s,t1,u,c,m,l,st,d1,d2=[],[],[],[],[],1,1,[],[],[],{},{}
#print(p)
a=primitive_root(p)
while len(r)!=n:
  x=random.randint(2,p-2)
  if x not in r:
    r.append(x)
while len(s)!=n:
  x=random.randint(2,p-2)
  if x not in s:
    s.append(x)
for i in range(n):
  t1.append(a ** r[i] % p)
  t2 = a ** s[i] % p
  l1.append(encrypt(p,r[i],t2))
for i in l1:
  c*=i
c%=p
for i in z:
  try:
      m.append(d1[i])
      l.append(chr(d1[i]))
  except:
      w=(c*i)%p
      d1[i]=w
      m.append(w)
      l.append(chr(w))
print("Encrypted Text Is",''.join(l))
for j in range(n):
  l2.append(decrypt(p,s[j],t1[j]))
for j in l2:
  u*=j
for j in m:
  try:
      st.append(d2[j])
  except:
      w=(u*j)%p
      d2[j]=chr(w)
      st.append(chr(w))
print("After Decryption :",''.join(st))




