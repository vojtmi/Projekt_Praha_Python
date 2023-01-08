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
            return select
        except ValueError:
            print('Neplatná volba, zkus to znovu')
        
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