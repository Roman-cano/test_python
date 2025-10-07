from mon_premier_projet.utilitaire import math
from mon_premier_projet.utilitaire import texte
from mon_premier_projet.utilitaire import convert
from mon_premier_projet.movies import movie


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
    quit = 1
    while(quit != 0):

        print("1 ajouter un film")
        print("2 supprimer un film")
        print("3 afficher les  film")
        quit = int(input("quit?"))

        if(quit == 1):
           film =  str(input("ajouter un film"))
           movie.add_movie(film)

        if(quit == 2 and len(movie.movie) > 0):
            movie.get_movie()
            index = int(input("saisissez l'index du film à supprimer"))
            movie.delete_movie(index)
        else:
            print("il n'y a aucun film a supprimer")

        if (quit == 3):
            movie.get_movie()




