from pojistnik import Pojistnik

pojisteni = []
konec = False

print("-" * 60)
print("Evidence pojištěných")
print("-" * 60)

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
        print("*"*60)
        print("Seznam pojištěných: ")
        print("*"*60)
        for klient in pojisteni:
            print(klient)
        print("*"*60)
        input("Pokračujte libovolnou klávesou... ")
        print("")
            
    elif vyber == 3:
        pass
    elif vyber == 4:
        konec = True
    else:
        print("Neplatná volba zkus znova")      
