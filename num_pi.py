from math import pi

def funpi(n):
    return f"{pi:.{n}f}"

n = int(input("Вывести число пи с точностью до (знаков после запятой): "))
print(funpi(n))



# или



from math import pi

def funpi(n):
    return "{pi:.{n}f}".format(pi=pi, n=n)

n = int(input("Вывести число пи с точностью до (знаков после запятой): "))
print(funpi(n))
