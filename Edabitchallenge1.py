def equalvalues(a, b, c):
    if a == b and a == c:
        return 3
    elif a == b or a == c:
        return 2
    else:
        return 0

print(equalvalues(2, 4, 2))