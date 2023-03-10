from pojistnik import Pojistnik
import os
class Akce():
    
    pojisteni = []
    # testovací subjekty
    testovaci = Pojistnik("Ivan", "Vopršálek", 38, 123456789)
    pojisteni.append(testovaci)
    testovaci = Pojistnik("Marek", "Nalezený", 32, 147852369)
    pojisteni.append(testovaci)
    # konec testovacích subjektů
    
    def selektor():
        try:
            select = int(input("Vyberte akci: "))
            if select in range(1,5):
                print("")
                return select
            else:
                er = True                
        except ValueError:
            er = True
        if er:
            input('Neplatná volba, zkus to znovu stisknutím klávesy. \n')
            os.system('cls')
        else:
            pass 
        
    def novyKlient():
        try:
            er = False
            jmeno = input("Zadejte jméno: ").capitalize()
            prijmeni = input("Zadejte příjmení: ").capitalize()
            vek = int(input("Zadejte věk: "))
            telefon = int(input("Zadejte telefoní číslo: "))
        except ValueError:
            er = True
        if not er and jmeno.isalpha() and prijmeni.isalpha():
            novy = Pojistnik(jmeno, prijmeni, vek, telefon)
            Akce.pojisteni.append(novy)
            input("Data jsou uložena. \nPokračujte libovolnou klávesou... ")
            print("")
        else:
            input("\n Něco se nepovedlo. \n Pokračuj libovolnou klávesou ...")
        
    def vypisPojistenych():
        
        for klient in Akce.pojisteni:
            print(klient)
    
    
    def vyhledej():
        
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        Akce.search_indices = [index for (index, item) in enumerate(Akce.pojisteni) 
                               if item.jmeno.lower() == jmeno.lower() or item.prijmeni.lower() == prijmeni.lower()]
    
    
    def vysledkyHledani():
        
        if len(Akce.search_indices) > 0:
            for i in Akce.search_indices:
                print(Akce.pojisteni[i])
        else:
            print("Nikdo takový tady není.")
            
            