a = list(map(str, input().split()))
print(all('a' in i.lower() for i in a))
