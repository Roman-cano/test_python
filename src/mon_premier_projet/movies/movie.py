movie = []


def add_movie(film):
    movie.append(film)


def print_movie():
    for i in range(len(movie)):
        print(i , movie[i])

def get_movies():
    return movie

def delete_movie(index):
     movie.pop(index-1)