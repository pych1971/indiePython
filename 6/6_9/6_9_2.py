vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
new_vector = [vector[i][j] for i in range(len(vector)) for j in range(len(vector[0]))]
print(new_vector)
