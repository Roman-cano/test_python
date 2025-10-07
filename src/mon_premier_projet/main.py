from mon_premier_projet.utilitaire import math
from mon_premier_projet.utilitaire import texte
from mon_premier_projet.utilitaire import convert

def dire_coucou():
    print("coucou !")

if __name__ == "__main__":
    dire_coucou()
    print(math.add(1 , 2))
    print(texte.upper("roman"))
    print(texte.lower("ROMAN"))
    print(convert.yen_euro(5))
    print(convert.euro_dollar(5))

    print("hello")
