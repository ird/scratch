def triplets(target):
    max = int(target/2)
    for a in range(1, max):
        for b in range(a, max):
            for c in range(b, max):
                if a*a + b*b == c*c:
                    # print("Triplet found: {} {} {}".format(a, b, c))
                    if a + b + c == target:
                        return (a, b, c)


print(triplets(1000))
