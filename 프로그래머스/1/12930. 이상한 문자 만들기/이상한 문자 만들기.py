def solution(s):
    word_list = s.split(' ')
    word_list = [list(i) for i in word_list]
    answer = []
    #[['t', 'r', 'y'], ['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]
    for word in word_list:
        for i in range(1,len(word)+1):
            if i%2 != 0:
                word[i-1] = word[i-1].upper()
            else:
                word[i-1] = word[i-1].lower()
        answer.append("".join(word))
    return " ".join(answer)