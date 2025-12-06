#son = int(input())
#son2 = int(input())
#son3 = son + son2
#print(son3)
##1-masala
#k = int(input("k = "))
#n = int(input("n = "))
#for i in range(n):
#    print(n)
#2-masala
#a = int(input("a = "))
#b = int(input("b = "))
#count = 0
#for i ni range(a, b+1)
#    print(i)
#    count = count + 1
#print("Sikl", count, "marta takrollanadi")
#3-masala
# ismlar = {"Bekmurod", "Suhrob", "Sulaymon"}
# print(ismlar)
# for  ismlar + {"Shahzod"}:
# print(for)



# #8-masala    a dan b gacha bo‘lgan barcha butun sonlarning ko‘paytmasini toping.
# a = int(input("a = "))
# b = int(input("b = "))

# p = 1
# for i in range(a, b + 1):
#     p *= i

# print("Ko‘paytma =", p)
# #9-masala  a dan b gacha bo‘lgan sonlarning kvadratlarining yig‘indisini hisoblash.
# a = int(input("a = "))
# b = int(input("b = "))

# s = 0
# for i in range(a, b + 1):
#     s += i * i

# print("Kvadratlar yig‘indisi =", s)



# #10-masala    n berilgan. Quyidagi yig‘indini hisoblash kerak:
# n = int(input("n = "))

# s = 0
# for i in range(1, n + 1):
#     s += 1 / i

# print("Yig‘indi =", s)

# #11-masala  n dan boshlab 2n gacha bo‘lgan barcha sonlarning kvadratlarini qo‘shish.
# n = int(input("n = "))

# s = 0
# for i in range(n, 2*n + 1):
#     s += i * i
# print("Yig‘indi =", s)

# #12-masala   n berilgan. Quyidagi ko‘paytmaga e’tibor bering:
# n = int(input("n = "))
# p = 1
# for i in range(1, n + 1):
#     p *= i
# print("Ko‘paytma =", p)


#####################################################################################################################

#13-masala
#n = int(input("n = "))
# n > 0
# S = 1
# for i in range(1, n + 1):
#      S *= i
# print("Ko‘paytma =", S)


# #2-m
# a = int(input("a = "))
# b = int(input("b = "))

# for i in range(a, b + 1):
#     print(i)
# #3-m
# a = int(input("a = "))
# b = int(input("b = "))

# for i in range(b, a - 1, -1):
#     print(i)

# #4-m
# p = float(input("1 kg narxi = "))

# for i in range(1, 10 + 1):
#     print(f"{i} kg = {p * i}")

# #5-m
# p = float(input("1 kg narxi = "))

# for i in range(1, 10):
#     kg = i / 10
#     print(f"{kg} kg = {p * kg}")
# #6-m
# p = float(input("1 kg narxi = "))

# kg = 1.2
# while kg <= 2.0:
#     print(f"{kg} kg = {p * kg}")
#     kg += 0.2

# #7-m

# a = int(input("a = "))
# b = int(input("b = "))

# s = 0
# for i in range(a, b + 1):
#     s += i

# print("Yig'indi =", s)


# #8-m
# a = int(input("a = "))
# b = int(input("b = "))

# p = 1
# for i in range(a, b + 1):
#     p *= i

# print("Ko'paytma =", p)


# ######################################################################################
# #While-1

# A = int(input("A sonni kiriting"))
# B = int(input("B sonni kiriting"))

# while A >= B :
#     A -= B
# print(A)

#W-2

#A = int(input("A sonni kiriting"))
#  B = int(input("B sonni kiriting"))

#  while A >= B :
#      A -= B
#      count = count + 1
#  print(count)

#while True :
#     yosh = int(input("Yoshni kiriting"))
#     if yosh <= 7 :
#        narx = 2000
#     elif yosh <= 18 :
#        narx = 3000
#     elif yosh <= 65 :
#        narx = 10_000
#     else :
#        narx = 0
# print(f"Sizning chipta narxingiz {narx} So'm")
# javob = input("Yoshni kiriting yoki dasturni tugarish uchun 'Exit' yoki 'Cuit' ")
# if (javob.lower() == 'quit' or javob.lower() == 'exit') :
#     break


kitoblar = []

print("Yaxshi ko'rgan kitoblaringizni kiriting. Tugatish uchun 'stop' deb yozing.")
while True:
    kitob = input("Kitob nomi: ")
    if kitob.lower() == "stop":
        break
    kitoblar.append(kitob)

print("\nSiz kiritgan kitoblar:")
for k in kitoblar:
    print("- " + k)


savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)

    # Dasturni to'xtatish
    if qiymat.lower() == "exit":
        break

    # Kiritilgan qiymat sonmi?
    try:
        son = float(qiymat)
    except ValueError:
        print("Iltimos, son kiriting!")
        continue

    # Manfiy sonni tekshirish
    if son < 0:
        print("Faqat musbat son kiriting!")
        continue

    # Ildizni hisoblash
    ildiz = son ** 0.5
    print(f"{son} ning ildizi {ildiz} ga teng")
