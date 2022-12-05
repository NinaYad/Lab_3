# O(nlogn)

def Qsort(mass):
    if len(mass) <= 1:
        return mass
    else:
        pillar = mass[0]
        SmallerThanPillar = []
        EqualPillar = []
        BiggerThanPillar = []
        for el in mass:
            if el < pillar:
                SmallerThanPillar.append(el)
            elif el > pillar:
                BiggerThanPillar.append(el)
            else:
                EqualPillar.append(el)
        return Qsort(SmallerThanPillar) + EqualPillar + Qsort(BiggerThanPillar)


# Придумать и реализовать алгоритмы, имеющие сложность O(nlogn), O(n!), O(3log(n))

# O(n**3)
def On3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                flag = True
    return ''

# O(2**n)

def DoubleRecursive(n):
    if n > 0:
        return DoubleRecursive(n - 1), DoubleRecursive(n - 1)
    return ''


# O(3n)

def O3n(n):
    if n > 0:
        print('')
        print('')
        print('')
    return ''
