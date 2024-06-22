import datetime


class ShowTime:
    def __init__(self, movie, date_time, price):
        self.movie = movie
        self.date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        self.price = price
        self.capacity = 100  # تعداد صندلی ها
        self.booked_seats = 0

    def is_available(self):
        if self.booked_seats < self.capacity:
            return True
        else:
            return False


# Set up showtimes
s1 = ShowTime("movie1", "2000-01-01 14:00", 10)
print(s1.capacity)
print(s1.is_available())



