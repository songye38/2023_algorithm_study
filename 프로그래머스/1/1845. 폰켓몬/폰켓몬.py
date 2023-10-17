import itertools
def solution(nums):
    if len(nums)//2 == len(set(nums)):
        return len(set(nums))
    elif len(nums)//2 < len(set(nums)):
        return len(nums)//2
    else:
        return len(set(nums))
    # answer_list = [0] * (len(nums)+1)
    # answer = set(itertools.combinations(nums,len(nums)//2))
    # #return max([len(list(set(i))) for i in answer])
    # return [i for i in answer]