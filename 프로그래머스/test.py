import itertools
import re
import copy

def solution(expression):
    answer = []
    operator = [i for i in ['*','+','-'] if i in list(expression)]
    
    combi = list(itertools.permutations(operator, len(operator)))
    expression = re.findall(r'(\d+|\D)', expression)

    #원본
    expression = [expression.strip() for expression in expression if expression.strip()]
    
    for i in combi:
        ex_copy = copy.deepcopy(expression)
        for j in range(len(i)-1):
            index = ex_copy.index(i[j])
            ex_copy.insert(index-1,'(')
            ex_copy.insert(index+3,')')
            result_str = "".join(ex_copy)
            try:
                temp_sum = eval(result_str)
                answer.append(abs(temp_sum))
                print(temp_sum)
            except (RuntimeError,SyntaxError,SyntaxWarning,TypeError):
                pass
    print(answer)
    return max(answer)

solution("100-200*300-500+20")