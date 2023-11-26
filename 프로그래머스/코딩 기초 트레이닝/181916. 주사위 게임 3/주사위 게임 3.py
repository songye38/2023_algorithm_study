def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        return 1111 * a
    elif a==b==c and d!=a:
        return ((10 * a) + d)**2
    elif a==b==d and c!=a:
        return ((10 * a) + c)**2
    elif a==c==d and b!=a:
        return ((10 * a) + b)**2
    elif b==c==d and a!=b:
        return ((10 * b) + a)**2
    elif a==b and c==d:
        return (a + c) * abs(a-c)
    elif a==c and b==d:
        return (a + b) * abs(a-b)
    elif a==d and b==c:
        return (a + b) * abs(a-b)
    elif b==c and a==d:
        return (b + a) * abs(b-a)
    elif b==d and a==c:
        return (b + a) * abs(b-a)
    elif c==d and a==b:
        return (c + a) * abs(c-a)
    elif a==b and a!=c!=d:
        return c * d
    elif a==c and a!=b!=d:
        return b * d
    elif a==d and a!=b!=c:
        return b * c
    elif b==c and b!=a!=d:
        return a * d
    elif b==d and b!=a!=c:
        return a * c
    elif c==d and c!=a!=b:
        return a * b
    elif a!=b!=c!=d:
        return min([a,b,c,d])
    #return answer