
notes = {}


def add_note(movie_id: str, note: float):
    if movie_id not in notes:
        notes[movie_id] = []

    movie_notes = notes[movie_id]
    movie_notes.append(note)

    notes[movie_id] = movie_notes


def get_best_movie():
    best_avg_movie_id = ""
    best_avg_note = 0

    for movie_id, movie_notes in notes.items():
        avg_note = sum(movie_notes) / len(movie_notes)

        if avg_note > best_avg_note:
            best_avg_note = avg_note
            best_avg_movie_id = movie_id

    return best_avg_movie_id