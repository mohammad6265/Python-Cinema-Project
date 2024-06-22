import datetime
from user import User


class Booking:
    def __init__(self, user, showtime):
        self.user = user
        self.showtime = showtime
        self.status = "pending"

    def book(self):
        current_time = datetime.datetime.now()
        if self.showtime < current_time:
            raise Exception("Showtime has already passed")
        if self.showtime.is_available():
            self.status = "confirmed"

        else:
            raise Exception("Showtime is not available")

    def cancel(self):
        if self.status == "confirmed":
            self.status = "cancelled"
            # Send cancellation notification
            # ...
        else:
            raise Exception("Cannot cancel booking")






