a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

valores = [a, b, c, d, e, f]
positivos = []

for i in valores:
    if i >= 0:
        positivos.append(i)

print(len(positivos), "valores positivos")
