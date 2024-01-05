days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
daysSorted = sorted(list(filter(lambda x: (len(x) == 4 or x[0] == 'S'), days)))
for i in daysSorted:
    print(i)
