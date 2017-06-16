def power(x,n):
        t=1
        if n==0:
            return 1
        elif n==1:
            return x
        t=power(x,n//2)
        print(t)
        if n%2==0:
            return t*t
        else:
            return x*t*t # 2^15 => 2 * 2^7 * 2^7
print(power(3,5))

