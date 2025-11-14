a, b, c = map(int, input().split())

if a >= b:
    c = b + 1

if c >= a:
    a += c
    if a >= b:
        a -= c
    else:
        c = b - c
else:
    if a == b:
        c = a - 7
    elif a > b:
        a = c * 2
    else:
        c = a % c
        
print(a, b, c)