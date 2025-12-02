#2-m
 a = int(input("a = "))
b = int(input("b = "))

for i in range(a, b + 1):
    print(i)
#3-m
a = int(input("a = "))
b = int(input("b = "))

for i in range(b, a - 1, -1):
    print(i)

#4-m
p = float(input("1 kg narxi = "))

for i in range(1, 10 + 1):
    print(f"{i} kg = {p * i}")

#5-m
p = float(input("1 kg narxi = "))

for i in range(1, 10):
    kg = i / 10
    print(f"{kg} kg = {p * kg}")
#6-m
p = float(input("1 kg narxi = "))

kg = 1.2
while kg <= 2.0:
    print(f"{kg} kg = {p * kg}")
    kg += 0.2

#7-m

a = int(input("a = "))
b = int(input("b = "))

s = 0
for i in range(a, b + 1):
    s += i

print("Yig'indi =", s)


#8-m
a = int(input("a = "))
b = int(input("b = "))

p = 1
for i in range(a, b + 1):
    p *= i

print("Ko'paytma =", p)



