import requests
import json

genre_list = {28 : "액션", 12: "모험", 16: "애니메이션", 35: "코미디",
    80 : "범죄", 99: "다큐멘터리", 18 : "드라마", 10751 : "가족",
    14 : "판타지", 36: "역사", 27: "공포", 10402 : "음악",
    9648 : "미스터리", 10749 : "로맨스", 878 : "SF", 10770 : "TV 영화",
    53 : "스릴러", 10752 : "전쟁", 37 : "서부"
}

class TMDBHelper:

    def get_requests_url(method, **kwargs):
        api_key = '8ffb4b999f9e6cb3f99f17488652cc28'

        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={api_key}'

        for key, value in kwargs.items() :
            request_url += f'&{key}={value}'

        return request_url
    

def get_top_rated():
    result = []
    ranking = 0
    for page in range(1, 2) :
        request_url=TMDBHelper.get_requests_url(method='/movie/now_playing', region='KR', language='ko', page=f'{page}')
        raw_data = requests.get(request_url).json()
        data = raw_data.get('results')
        for movie in data:
            ranking += 1
            genre_names = []
            for genre in movie.get('genre_ids'):
                genre_names.append(genre_list[genre])
            movie_dict = {
                'model' : 'movies.now_movie',
                'pk': movie.get('id'),
                'fields' : {
                    'title' : movie.get('title'),
                    'overview' : movie.get('overview'),
                    'popularity' : movie.get('popularity'),
                    'vote_count' : movie.get('vote_count'),
                    'vote_average' : movie.get('vote_average'),
                    'release_date' : movie.get('release_date'),
                    'poster_path' : movie.get('poster_path'),
                    'backdrop_path' : movie.get('backdrop_path'),
                    'genres' : genre_names,
                    'year' : int(movie.get('release_date')[:4]),
                    'ranking' : ranking,
                }
            }
            result.append(movie_dict)
    return result

with open('./movies/fixtures/now_playing.json', 'w', encoding='UTF-8') as f:
    json.dump(get_top_rated(), f, ensure_ascii=False, indent=2)