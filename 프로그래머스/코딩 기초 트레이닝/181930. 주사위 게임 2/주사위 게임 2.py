def solution(a, b, c):
    if a != b and a!=c and b != c:
        return a + b + c
    elif a == b and b != c:
        return (a + b + c) * (a**2 + b ** 2 + c**2)
    elif a==c and a!=b:
        return (a + b + c) * (a**2 + b ** 2 + c**2)
    elif b==c and a !=b:
        return (a + b + c) * (a**2 + b ** 2 + c**2)
    elif a==b==c:
        return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)