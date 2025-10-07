from mon_premier_projet.movies import movie
from mon_premier_projet.movies.movie import get_movies, add_movie, print_movie
from mon_premier_projet.notes import notes
from mon_premier_projet.notes.notes import add_note, get_best_movie

if __name__ == "__main__":
    quit = 1

    while(quit != 0):

        print("1 ajouter un film")
        print("2 supprimer un film")
        print("3 afficher les  film")
        print("4 ajouter une note à un film")
        print("5 récupérer le nom du meilleur film")

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
            print_movie()

        if quit == 4:
            movie_name = str(input("Indiquez le film à noter :"))
            movie_note = float(input("Indiquez la note :"))

            movies = get_movies()
            if movie_name not in movies:
                print("il n'y a aucun film a supprimer")
            else:
                add_note(movie_name, movie_note)
                print("La note a bien été ajouté")

        if quit == 5:
            print(get_best_movie())


