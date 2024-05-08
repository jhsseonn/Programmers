def solution(genres, plays):
    answer = []

    genres_dict = {}
    songs_dict = {}
    songs_genre_dict = {}

    for i in range(len(plays)):
        genres_keys = genres_dict.keys()
        if genres[i] in genres_keys:
            genres_dict[genres[i]] += plays[i]
            print(genres_dict[genres[i]])
        else:
            genres_dict[genres[i]] = plays[i]
            print(genres_dict[genres[i]])

        songs_dict[i] = plays[i]
        songs_genre_dict[i] = genres[i]

    genres_dict = dict(sorted(genres_dict.items(), key=lambda x: x[1], reverse=True))
    songs_dict = dict(sorted(songs_dict.items(), key=lambda x: x[1], reverse=True))
    print(genres_dict)
    print(songs_genre_dict)
    print(songs_dict)

    for genre in genres_dict.keys():
        songs = []
        for k, v in songs_dict.items():
            if songs_genre_dict[k] == genre and len(songs) < 2:
                songs.append(k)
                print(k)
            else:
                continue
        print(songs)
        answer.extend(songs)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
