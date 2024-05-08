from abc import ABC, abstractmethod
from datetime import datetime

# Absztrakt Szoba osztály
class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def tipus(self):
        pass

# Egyágyas szoba
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)  # Példa ár

    def tipus(self):
        return "Egyágyas szoba"

# Kétágyas szoba
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # Példa ár

    def tipus(self):
        return "Kétágyas szoba"

# Foglalás osztály
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Szobaszám: {self.szoba.szobaszam}, Típus: {self.szoba.tipus()}, Dátum: {self.datum}, Ár: {self.szoba.ar} HUF"

# Szálloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def hozzad_szoba(self, szoba):
        self.szobak.append(szoba)

    def listaz_szobak(self):
        if not self.szobak:
            print("Nincsenek elérhető szobák.")
            return
        print("\nElérhető szobák a szállodában:")
        for szoba in self.szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Típus: {szoba.tipus()}, Ár: {szoba.ar} HUF")

    def foglal_szoba(self, szobaszam, datum):
        try:
            foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
            if foglalas_datum.date() < datetime.now().date():
                print("Érvénytelen foglalás, múltbéli időpont miatt.")
                return
        except ValueError:
            print("Hibás dátum formátum! Használj ÉÉÉÉ-HH-NN formátumot.")
            return

        szoba = next((s for s in self.szobak if s.szobaszam == szobaszam), None)
        if not szoba:
            print("Nincs ilyen szoba!")
            return

        if any(f for f in self.foglalasok if f.szoba.szobaszam == szobaszam and f.datum == datum):
            print("A szoba már foglalt ezen a napon!")
            return

        uj_foglalas = Foglalas(szoba, datum)
        self.foglalasok.append(uj_foglalas)
        print(f"Foglalás megtörtént: {uj_foglalas}")

    def lemond_foglalas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás lemondva: {foglalas}")
                return
        print("Nincs ilyen foglalás!")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("\nNincsenek foglalások.")
            return
        print("\nJelenlegi foglalások:")
        for foglalas in self.foglalasok:
            print(foglalas)

# Felhasználói interfész
def felhasznaloi_interfesz():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.hozzad_szoba(EgyagyasSzoba(101))
    szalloda.hozzad_szoba(EgyagyasSzoba(102))
    szalloda.hozzad_szoba(KetagyasSzoba(201))

    # Előre beállított foglalások
    szalloda.foglal_szoba(101, "2024-05-12")
    szalloda.foglal_szoba(102, "2024-05-13")
    szalloda.foglal_szoba(201, "2024-05-14")
    szalloda.foglal_szoba(101, "2024-05-15")
    szalloda.foglal_szoba(102, "2024-05-16")

    print("\nÜdvözöljük a", szalloda.nev, "foglalási rendszerében!")
    szalloda.listaz_szobak()
    szalloda.listaz_foglalasok()

    while True:
        print("\nVálassz egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasz = input("Választás: ")

        if valasz == "1":
            szobaszam = int(input("Add meg a szobaszámot: "))
            datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")
            szalloda.foglal_szoba(szobaszam, datum)

        elif valasz == "2":
            szobaszam = int(input("Add meg a szobaszámot: "))
            datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")
            szalloda.lemond_foglalas(szobaszam, datum)

        elif valasz == "3":
            szalloda.listaz_foglalasok()

        elif valasz == "4":
            break

        else:
            print("Érvénytelen választás, próbáld újra.")

if __name__ == "__main__":
    felhasznaloi_interfesz()
