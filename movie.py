import uuid
from datetime import datetime
from user import User
import datetime


class Movie:
    """Movie information"""
    """اطلاعات فیلم"""
    movies = {}

    def __init__(self, title: str, director: str, release_year: int, genre: str, movie_time_passed):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.movie_time_passed = movie_time_passed
        self._id = str(uuid.uuid4())

    @classmethod
    def add_movie(cls, movie: "Movie"):
        if movie.title in cls.movies:
            print(f"Movie '{movie.title}' is already in the database.")
            return False
        else:
            cls.movies[movie.title] = movie
            return True

    @classmethod
    def search_movie(cls, title: str):
        if title in cls.movies:
            return cls.movies[title]
        else:
            print(f"Movie '{title}' not found.")
            return None

    @classmethod
    def list_movies(cls):
        if not cls.movies:
            print("No movies found.")
            return
        for movie in cls.movies.values():
            print(f"Title: {movie.title}\nDirector: {movie.director}\nRelease Year: {movie.release_year}"
                  f"\nGenre: {movie.genre}\n")

    def __str__(self) -> str:
        return (f"Title: {self.title}\nDirector: {self.director}"
                f"\nRelease Year: {self.release_year}\nGenre: {self.genre}")


class TicketReservationSystem:
    """Ticket reservation system"""
    """سیستم رزرو بلیط"""

    def __init__(self):
        self.movies = Movie.movies
        self.tickets = {}

    def reserve_ticket(self, user: "User", movie_title: str, seat_number: int):
        if movie_title not in self.movies:
            print(f"Movie '{movie_title}' not found.")
            return False

        ticket_id = str(uuid.uuid4())
        ticket = {
            'user': user,
            'movie': self.movies[movie_title],
            'seat_number': seat_number,
            'reservation_date': datetime.now()
        }
        self.tickets[ticket_id] = ticket
        print(f"Ticket reserved successfully! Ticket ID: {ticket_id}")
        return True

    def cancel_ticket(self, ticket_id: str):
        if ticket_id not in self.tickets:
            print(f"Ticket with ID '{ticket_id}' not found.")
            return False

        del self.tickets[ticket_id]
        print(f"Ticket with ID '{ticket_id}' canceled successfully.")
        return True

    def view_tickets(self, user: "User", ticket_id=None):
        user_tickets = [ticket for ticket in self.tickets.values() if ticket['user'] == user]
        if not user_tickets:
            print("No tickets found for this user.")
            return

        for ticket in user_tickets:
            print(f"Ticket ID: {ticket_id}\nMovie: {ticket['movie'].title}"
                  f"\nSeat Number: {ticket['seat_number']}"
                  f"\nReservation Date: {ticket['reservation_date']}\n")



# Add movies
movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama")
Movie.add_movie(movie1)

movie2 = Movie("The Godfather", "Francis Ford Coppola", 1972, "Crime")
Movie.add_movie(movie2)

# Search for a movie
found_movie = Movie.search_movie("The Godfather")
if found_movie:
    print(found_movie)

# List all movies
Movie.list_movies()
