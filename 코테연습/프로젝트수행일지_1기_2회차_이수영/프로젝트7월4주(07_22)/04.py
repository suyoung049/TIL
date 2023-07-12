import requests
from pprint import pprint

def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key':'dcc1e7ed069f7427a2816e92b32e7c8b',
        'language': 'ko-KR',
        'query': title
        }
    response = requests.get(BASE_URL+path, params = params).json()
    movies = response.get('results')
    if movies ==[]:
        result = 'none'
    else:
        first_id = movies[0]['id']
        path_2 = f'/movie/{first_id}/recommendations'
        params = {
            'api_key':'dcc1e7ed069f7427a2816e92b32e7c8b',
            'language': 'ko-KR'
            }
        response = requests.get(BASE_URL+path_2, params = params).json()
        movies = response.get('results')
        result = []
        for movie in movies:
            result.append(movie['title'])
        return result  

    
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
