permutations = [1,2,3]

for x in permutations:
    for y in permutations:
        for z in permutations:
            if x != y and y != z and x != z:
                print(str(x) + str(y) + str(z))