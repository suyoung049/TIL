import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/search/movie'

params = {
    'api_key': 'dcc1e7ed069f7427a2816e92b32e7c8b',
    'language': 'ko-KR',
    'query': '기생충'
}

response = requests.get(BASE_URL+path, params = params).json()

movies = response.get('results')

first_id = movies[0]['id']

path_2 = f'/movie/{first_id}/credits'
params = {
    'api_key': 'dcc1e7ed069f7427a2816e92b32e7c8b',
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path_2, params = params).json()
casts = response.get('cast')
crews = response.get('crew')
main = []
for cast in casts:
    if cast['cast_id'] < 10:
        main.append(cast)
Fame = []
for act in main:
    Fame.append(act['name'])
people = []
for crew in crews:
    if crew['department'] == 'Directing':
        people.append(crew)

emp = []
for person in people:
    emp.append(person['name'])
all ={'cast': Fame, 'crew': emp}
print(all)

