class Rozhrani:
    # Jednotný násobič znaků v rozhraní
    znakovac = 60
        
    def head() -> str:
        
        print("-" * Rozhrani.znakovac)
        print("Evidence pojištěných")
        print("-" * Rozhrani.znakovac)
        
    def select_UI() -> str:
        
        print("1 - Přidat nového pojistěnce")
        print("2 - Vypsat vsechny pojistene")
        print("3 - Vyhledat pojistneho")
        print("4 - Konec \n")
    
        
    def pridat_novy():
        
        print("*" * Rozhrani.znakovac)
        print("Přidání nového pojištěnce: ")
        print("*" * Rozhrani.znakovac)
        
        
    def seznam_head():
        
        print("*" * Rozhrani.znakovac)
        print("Seznam pojištěných: ")
        print("*" * Rozhrani.znakovac)
        
        
    def seznam_foot():
        
        print("*" * Rozhrani.znakovac)
        input("Pokračujte libovolnou klávesou... \n")
        print("")
        
        
    def vyhledej_head():
        
        print("*" * Rozhrani.znakovac)
        print("Zahajuji vyhledávání")
        print("*" * Rozhrani.znakovac)
        
    
    def vyhledej_mid():
        
        print("*" * Rozhrani.znakovac)
        print("Výsledky vyhledávání:")
        print("*" * Rozhrani.znakovac)
        
        
    def vyhledej_foot():
          
        print("*" * Rozhrani.znakovac)
        input("Pokračujte libovolnou klávesou... ")
        print("") 
        
        