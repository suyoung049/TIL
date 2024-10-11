genres, plays = ["classic", "pop", "classic", "classic", "pop"], 	[500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    time_dict = dict()
    song_dict = dict()
    for i in range(len(genres)):
        if time_dict.__contains__(genres[i]):
            time_dict[genres[i]] += plays[i]
            song_dict[genres[i]].append((i, plays[i]))
        else:
            time_dict[genres[i]] = plays[i]
            song_dict[genres[i]] = [(i, plays[i])]
    sort_play = sorted(time_dict, key=lambda x:time_dict[x], reverse=True)
    for genre in sort_play:
        sort_genre = sorted(song_dict[genre], key=lambda x:(-x[1], x[0]))
        if len(sort_genre) < 2:
            answer.append(sort_genre[0][0])
        else:
            for i in range(2):
                answer.append(sort_genre[i][0])
    
       
    return answer


solution(genres, plays)