from pojistnik import Pojistnik

pojisteni = []
konec = False
znakovac = 60

print("-" * znakovac)
print("Evidence pojištěných")
print("-" * znakovac)

prvni = Pojistnik("Ivan", "Vopršálek", 38, 123456789)
pojisteni.append(prvni)

while not konec:
    print("Vyberte si akci: ")
    print("1 - Přidat nového pojistěnce")
    print("2 - Vypsat vsechny pojistene")
    print("3 - Vyhledat pojistneho")
    print("4 - Konec")
    vyber = int(input())
    if vyber == 1:
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = int(input("Zadejte telefoní číslo: "))

        novy = Pojistnik(jmeno, prijmeni, vek, telefon)
        pojisteni.append(novy)
        input("Data jsou uložena. Pokračujte libovolnou klávesou... ")
        print("")

    elif vyber == 2:
        print("*" * znakovac)
        print("Seznam pojištěných: ")
        print("*"*znakovac)
        for klient in pojisteni:
            print(klient)
        print("*" * znakovac)
        input("Pokračujte libovolnou klávesou... ")
        print("")
            
    elif vyber == 3:
        print("*" * znakovac)
        print("Zahajuji vyhledávání")
        print("*" * znakovac)
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        search_indices = [index for (index, item) in enumerate(pojisteni) if item.jmeno == jmeno or item.prijmeni]
                
        print(search_indices)
        print("*" * znakovac)
        input("Pokračujte libovolnou klávesou... ")
        print("")
                
    elif vyber == 4:
        konec = True
    else:
        print("Neplatná volba zkus znova")      
