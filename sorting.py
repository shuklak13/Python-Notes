print(sorted([1, 3, 2]))               #[1, 2, 3]
print(sorted([1, 3, 2], reverse=True)) #[3, 2, 1]

#[(0,1), (4,0), (7,2)]
print(sorted([(7, 2), (4, 0), (0, 1)], key = lambda x: x[0]))