from pojistnik import Pojistnik
import time

pojisteni = []
konec = False
znakovac = 60
pause = time.sleep(1)

print("-" * znakovac)
print("Evidence pojištěných")
print("-" * znakovac)

prvni = Pojistnik("Ivan", "Vopršálek", 38, 123456789)
pojisteni.append(prvni)
prvni = Pojistnik("Marek", "Nalezený", 32, 147852369)
pojisteni.append(prvni)

while not konec:
    print("Vyberte si akci: ")
    print("1 - Přidat nového pojistěnce")
    print("2 - Vypsat vsechny pojistene")
    print("3 - Vyhledat pojistneho")
    print("4 - Konec")
    try:
        vyber = int(input())
    except ValueError:
        print("Neplatná volba")
        continue
    if vyber == 1:
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        try:
            vek = int(input("Zadejte věk: "))
            telefon = int(input("Zadejte telefoní číslo: "))
        except ValueError:
            print("\n Nemělo by to být náhodou číslo?\n Zkus to znovu.\n")
            continue

        novy = Pojistnik(jmeno, prijmeni, vek, telefon)
        pojisteni.append(novy)
        pause
        input("Data jsou uložena. Pokračujte libovolnou klávesou... ")
        print("")

    elif vyber == 2:
        print("*" * znakovac)
        print("Seznam pojištěných: ")
        print("*"*znakovac)
        pause
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
        search_indices = [index for (index, item) in enumerate(pojisteni) if item.jmeno == jmeno or item.prijmeni == prijmeni]
        print("*" * znakovac)
        pause
        if len(search_indices) > 0:
            for i in search_indices:
                print(pojisteni[i])
        else:
            print("Nikdo takový tady není.")
        print("*" * znakovac)
        input("Pokračujte libovolnou klávesou... ")
        print("")
                
    elif vyber == 4:
        konec = True
    else:
        print("Neplatná volba zkus znova")      
