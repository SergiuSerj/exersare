result = list()
lungime = int
lista_introdusa = []


def function_separat(lista_introdusa, lungime):
    return lista_introdusa[:lungime], lista_introdusa[lungime:]

while True:
    introducere_date = input("Va rog introduceti numere in lista. Pentru terminare dati Enter: ")
    if introducere_date.isdigit():
        introducere_date = int(introducere_date)
        lista_introdusa.append(introducere_date)
        print(lista_introdusa)
    elif introducere_date == "":
        break
    else:
        print("nu ati introdus un numar")
        print("Lista este: \n", lista_introdusa)
        continue




while True:
    lungime = input("Indruceti lungimea listei: ").strip()
    if len(lista_introdusa) > int(lungime) and lungime.isdigit():
        lungime = int(lungime)
        print(function_separat(lista_introdusa, lungime))
        break
    if len(lista_introdusa) < int(lungime) :
        print("Numarul introdus pentru lungime este mai mare decat lungimea listei.")
        print(lista_introdusa)






