from pojistnik import Pojistnik
class Rozhrani:
    znakovac = 60
    pojisteni = []
    
    def head() -> str:
        print("-" * Rozhrani.znakovac)
        print("Evidence pojištěných")
        print("-" * Rozhrani.znakovac)
        
    def select_UI() -> str:
        print("Vyberte si akci: ")
        print("1 - Přidat nového pojistěnce")
        print("2 - Vypsat vsechny pojistene")
        print("3 - Vyhledat pojistneho")
        print("4 - Konec")
    
    def select(select = 4) -> int:
        try:
            select = int(input())
            if select in range(1,5):
                return select
            else:
                erorek = True                
        except ValueError:
            erorek = True
        if erorek:
            print('Neplatná volba, zkus to znovu. \n')
        else:
           pass 
        
    def pridat_novy():
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        try:
            vek = int(input("Zadejte věk: "))
            telefon = int(input("Zadejte telefoní číslo: "))
        except ValueError:
            print("\n Nemělo by to být náhodou číslo?\n Zkus to znovu.\n")
            erorek = True
        if not erorek:
            novy = Pojistnik(jmeno, prijmeni, vek, telefon)
            Rozhrani.pojisteni.append(novy)
            input("Data jsou uložena. Pokračujte libovolnou klávesou... ")
            print("")
        else:
            pass
        
    def seznam():
        print("*" * Rozhrani.znakovac)
        print("Seznam pojištěných: ")
        print("*" * Rozhrani.znakovac)
        for klient in Rozhrani.pojisteni:
            print(klient)
        print("*" * Rozhrani.znakovac)
        input("Pokračujte libovolnou klávesou... ")
        print("")
        
    def vyhledat():
        print("*" * Rozhrani.znakovac)
        print("Zahajuji vyhledávání")
        print("*" * Rozhrani.znakovac)
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        search_indices = [index for (index, item) in enumerate(Rozhrani.pojisteni) if item.jmeno == jmeno or item.prijmeni == prijmeni]
        print("*" * Rozhrani.znakovac)
        
        if len(search_indices) > 0:
            for i in search_indices:
                print(Rozhrani.pojisteni[i])
        else:
            print("Nikdo takový tady není.")
        print("*" * Rozhrani.znakovac)
        input("Pokračujte libovolnou klávesou... ")
        print("") 