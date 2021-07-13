#to jest program z ćwiczeniem na dictonary :-)
lista_zakupow = {}


def dodawanie_produkt():
    produkt = input("Podaj nazwę produktu:  ")
    print("")
    cena = input("Podaj cenę produktu:  ")
    print("")
    lista_zakupow[produkt] = cena
    print("")


def wysw_liste():
    print("Twoja lista zakupów wygląda następująco: \n")
    a = 1
    for produkt1 in lista_zakupow.keys():
        print(a, ".", produkt1)
        a += +1
    print("")


def koszt_zakupow():
    cena_razem = 0
    for cena1 in lista_zakupow.values():
        cena_razem = cena_razem + float(cena1)
    print("Twoje zakupy kosztują:", cena_razem, "zł.")
    print("")


print("")
print("Witaj. Zapraszam Cię na zakupy :-)\n")

dodawanie_produkt()
dodawanie_produkt()
dodawanie_produkt()
dodawanie_produkt()
dodawanie_produkt()

wysw_liste()

koszt_zakupow()

