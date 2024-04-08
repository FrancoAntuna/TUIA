def mayor(l: list[int], m):
    if len(l) >= 1: 
        if l[0] >= m:
            m = l[0]
            return mayor(l[1:], m)
        return mayor(l[1:], m)
    return m
pass

def mayorv2(l:list[int]):
    if len(l) == 1:
        return l[0]
    a1 = l[0]
    a2 = l[1:]
    a2n = mayorv2(a2)
    if a1 > a2n:
        return a1
    else:
        return a2n

l = [1, 2, 4, 5, 2, 6, 1, 7, 2, 4, 5, 8, 4, 9, 2, 4, 123, 2, 6, 61, 1251, 564351, 342]
m = l[0]
max = mayor(l, m)
print(max)
max = mayorv2(l)
print(max)
