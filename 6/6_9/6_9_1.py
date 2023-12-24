colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']
a = [(colors[i], sizes[j]) for i in range(len(colors)) for j in range(len(sizes))]
print(a)
