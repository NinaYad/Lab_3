l = list(map(int, input().split(' ')))
d = [12, 5, 6, 23, 75, 8, 34, 6, 2, 1]
def bubblesort(l):
    for i in range(len(l)):
        for j in range(1, len(l) - i):
            if l[j] < l[j - 1]:
                a = l[j]
                l[j] = l[j - 1]
                l[j - 1] = a
    return l


print(bubblesort(d))