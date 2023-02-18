cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
result = 0
cache = []

for city in cities:
    city = city.lower()
    if city in cache:
        cache.pop(cache.index(city))
        cache.append(city)
        result += 1 
    
    else:
        if len(cache) < cacheSize:
                cache.append(city)

        elif len(cache) == cacheSize:
            cache.append(city)
            cache.pop(0)
        result += 5
print(result)