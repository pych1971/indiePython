a = list(map(str, input().split()))
print(any(i[-5:].lower() == 'ought' for i in a))
