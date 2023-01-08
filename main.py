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
        Rozhrani.seznam()
            
    elif vyber == 3:
        Rozhrani.vyhledat()
                
    elif vyber == 4:
        konec = True
        print("")
      
