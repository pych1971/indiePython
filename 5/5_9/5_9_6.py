st = 'Create a list of the first letters of every word in this string'
a = st.split()
b = [a[i][0] for i in range(len(a))]
print(b)
