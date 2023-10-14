def down(n1,n2):
    if n1 and n2:
        return True
    elif n1 and not n2:
        return True
    elif not n1 and n2:
        return True
    else:
        return False
    
def up(n1,n2):
    if n1 and n2:
        return True
    elif n1 and not n2:
        return False
    elif not n1 and n2:
        return False
    else:
        return False
    
    
def solution(x1, x2, x3, x4):
    return up(down(x1,x2),down(x3,x4))