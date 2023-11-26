def solution(spell, dic):
    spell.sort()
    spell = "".join(spell)
    new_dic = []
    for i in dic:
        temp = sorted(i)
        new_dic.append("".join(temp))
    for i in new_dic:
        if spell == i:
            return 1
        
    return 2