def solution(n):
    sum = 0
    if n %2==0:
        numbers = [i for i in range(1,n+1) if i%2==0]
        for i in numbers:
            sum += i ** 2
        return sum
    else:
        numbers = [i for i in range(1,n+1) if i%2!=0]
        for i in numbers:
            sum += i
        return sum