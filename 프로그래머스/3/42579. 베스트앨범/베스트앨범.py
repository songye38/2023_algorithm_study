def solution(genres, plays):
    genre_dict = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = {'total_count': plays[i], 'songs_list': [[i,plays[i]]]}
        else:
            genre_dict[genres[i]]['total_count'] += plays[i]
            genre_dict[genres[i]]['songs_list'].append([i,plays[i]])
        
    
    genre_dict = dict(sorted(genre_dict.items(),key = lambda x : x[1]['total_count'],reverse=True))
    for genre in genre_dict:
        genre_dict[genre]['songs_list'] = sorted(genre_dict[genre]['songs_list'],key=lambda x : x[1],reverse=True)
        

    
    for genre in genre_dict:
        count = 0
        for song in genre_dict[genre]['songs_list']:
            count +=1
            if count >2:
                continue
            else:
                answer.append(song[0])
    return answer
    
    
    
    
    
    