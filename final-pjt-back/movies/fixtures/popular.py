import requests
import json

class TMDBHelper:

    def get_requests_url(method='/movie/popular', **kwargs):
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
    for page in range(1, 500) :
        request_url=TMDBHelper.get_requests_url(method='/movie/top_rated', region='KR', language='ko', page=f'{page}')
        raw_data = requests.get(request_url).json()
        data = raw_data.get('results')
        for movie in data:
            ranking += 1
            # for genre in movie.get('genre_ids'):
            #     genre_names.append(genre_list[genre])
            movie_dict = {
                'model' : 'movies.movie',
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
                    'genres' : movie.get('genre_ids'),
                    'year' : int(movie.get('release_date')[:4]),
                    'ranking' : ranking,
                    'isPicked' : False,
                }
            }
            result.append(movie_dict)
    return result

with open('./final-pjt-back/movies/fixtures/movies.json', 'w', encoding='UTF-8') as f:
    json.dump(get_top_rated(), f, ensure_ascii=False, indent=2)