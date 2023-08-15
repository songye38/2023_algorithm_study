n = int(input())
m = int(input())
numbers = list(map(int,input().split()))

count = 0
start_index = 0
end_index = n-1

#리스트 sorting
numbers.sort()
print(numbers)

while start_index<end_index:
    if numbers[start_index]+numbers[end_index] < m:
        start_index+=1
    elif numbers[start_index]+numbers[end_index] > m:
        end_index-=1
    else:
        start_index+=1
        end_index-=1
        count+=1


print(count)

