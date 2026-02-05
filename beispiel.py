class Tier:
    def __init__(self,name: str, alter: str):
        self.name = name
        self.alter = alter
    
    def macht_geräusche(self):
        print(f"{self.name} macht ein Geräusch")

    def beschreibung(self):
        print(f" DAs ist {self.name}. Es ist {self.alter} Jahre alt")
    
    def __str__(self) -> str:
        return f"Tier: {self.name}, Alter: {self.alter}"
    

class hund(Tier):
    def macht_geräusche(self):
        print(f"Tier {self.name} bellt")

class katze(Tier):
    def __init__(self,name: str, alter: str):
        super().__init__(name, alter)
        print(f" mit {name} wurde eine neue Katze erstellt")

    def macht_geräusche(self):
        print(f"{self.name} miaut")


hund1=hund ("Bello", "3")
whiskas = katze("whiskas", "4")
print(hund1)
hund1.macht_geräusche()
whiskas.macht_geräusche()
