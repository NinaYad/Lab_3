import itertools

n = int(input())

# O(n**3)

for i in range(n):
    for j in range(n):
        for k in range(n):
            flag = True


# O(2**n)

def DoubleRecursive(n):
    if n > 0:
        DoubleRecursive(n - 1)
        DoubleRecursive(n - 1)
    return ''


# O(3n)

for i in range(n):
    print('/')
for i in range(n):
    print('/')
for i in range(n):
    print('/')

# O(3logn)

a = list(i for i in range(n))
a.remove(0)
a.remove(2)
a.remove(1)
print(a)

# O(nlogn)

a = list(i for i in range(n))
a.sort()
print(a)

# O(n!)

perm_set = itertools.permutations(a)
for i in perm_set:
    print(i)
