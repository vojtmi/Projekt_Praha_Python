from rozhrani import Rozhrani
from akce import Akce
import os
 
class App():
    
    def start():
        os.system('cls')
        konec = False
        while not konec:
            Rozhrani.head()
            Rozhrani.select_UI()
            vyber = Akce.selektor() 
            
            if vyber == 1:
                Rozhrani.pridat_novy()
                Akce.novyKlient()
                os.system('cls')
                continue
            
            elif vyber == 2:
                Rozhrani.seznam_head()
                Akce.vypisPojistenych()
                Rozhrani.seznam_foot()
                os.system('cls')
                    
            elif vyber == 3:
                Rozhrani.vyhledej_head()
                Akce.vyhledej()
                Rozhrani.vyhledej_mid()
                Akce.vysledkyHledani()
                Rozhrani.vyhledej_foot()
                os.system('cls')
                        
            elif vyber == 4:
                konec = True
                os.system('cls')
                print("Děkuji za použití aplikace. :)")
                
                               
                