class Pojistnik():
    
    def __init__(self, jmeno: str, prijmeni: str, vek: int, telefon: int) -> None:
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        
    def __str__(self) -> str:
        return "{0} \t {1} \t {2} \t {3}".format(self.jmeno, self.prijmeni, self.vek, self.telefon)
    
    