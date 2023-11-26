def solution(polynomial):
    val_x = 0
    num = 0
    poly = polynomial.split(' ')
    for i in poly:
        if i[-1]=='x':
            if len(i)==1:
                val_x += 1
            else:
                val_x += int(i[:-1])
        elif i=='+':
            continue
        else:
            num += int(i)
    print(val_x,num)
    if num==0 and val_x!=1:
        return str(val_x) +'x'
    elif val_x==0:
        return str(num)
    elif val_x==1 and num!=0:
        return 'x' + ' + ' + str(num)
    
    elif val_x==1 and num==0:
        return 'x'
    else:
        return str(val_x) + 'x' + ' + ' + str(num)
            