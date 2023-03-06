def suma(tuplu):
    test = list(tuplu)
    count = 0
    for i in test:
        count += i
    return count


tuplu = (8, 2, 3, 0, 7)
print(suma(tuplu))

# dictionar = {}
#
# while len(dictionar) < 21:
#     while True:
#         try:
#             numar_introdus = int(input("Introduceti un numar intreg pozitiv: "))
#             break
#         except:
#             print("Nu este un numar intreg pozitiv")
#             continue



