a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for x in range(len(a)):
    for y in range(len(b[0])):
        for z in range(len(b)):
            result[x][y] += a[x][z] * b[z][y]
for x in range(len(result)):
    result[x] = tuple(result[x])
result = tuple(result)
for x in range(len(result)):
    print(result[x])