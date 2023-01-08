from pojistnik import Pojistnik
from rozhrani import Rozhrani
import time

pojisteni = Rozhrani.pojisteni
konec = False
znakovac = 60
pause = time.sleep(1)

Rozhrani.head()

prvni = Pojistnik("Ivan", "Vopršálek", 38, 123456789)
pojisteni.append(prvni)
prvni = Pojistnik("Marek", "Nalezený", 32, 147852369)
pojisteni.append(prvni)

while not konec:
    Rozhrani.select_UI()
    vyber = Rozhrani.select() 
    
    if vyber == 1:
        Rozhrani.pridat_novy()
        continue
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
        print("")
    else:
        print("Neplatná volba zkus znova")      
