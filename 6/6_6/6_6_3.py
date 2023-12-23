countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
ans = f'ERROR: Country for {city} not found'
for i in countries:
    if city in countries[i]:
        ans = f'INFO: {city} is a city in {i}'
        break
print(ans)
