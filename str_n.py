def fun(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s

s = input()
n = int(input())
print(fun(s, n))
