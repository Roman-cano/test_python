movie = []


def add_movie(film):
    movie.append(film)


def get_movie():
    for i in range(len(movie)):
        print(i , movie[i])


def delete_movie(index):
     movie.pop(index-1)