from datetime import datetime
from movie import Movie
import uuid
import hashlib
import getpass


class User:
    """User creation form"""
    """فرم ساخت کاربر"""
    users = {}

    def __init__(self, username: str, password: str, birthday: str, phone_number=None):
        self.username = username
        self._password = password
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
        self.phone_number = phone_number
        self.age = datetime.now() - self.birthday
        self._id = str(uuid.uuid4())
        self.registration_date = datetime.now()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password, users=None):
        """Creating a password and its correctness"""
        """ایجاد پسورد و صحیح بودن آن"""
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        if password == self.username:
            raise ValueError("Password cannot be the same as the username.")
        if password in users.values():
            raise ValueError("Password cannot be repeated.")
        self._password = self._hash_password(password)

    @staticmethod
    def _hash_password(password: str):
        """ Hash the password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def register_user(cls):
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        birthday = input("enter your birthday (YYYY-MM-DD):")
        phone_number = input("Enter a phone number (optional): ")
        if not birthday:
            print("Birthday is required.")
            return

        try:
            datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
            return

        new_user = cls(username, password, birthday, phone_number)
        if cls.add_user(new_user):
            print("User registered successfully!")
        else:
            print("Failed to register user.")

    @classmethod
    def add_user(cls, user: "User"):
        if user.username in cls.users:
            print(f"Username '{user.username}' is already taken.")
            return False
        else:
            cls.users[user.username] = user
            return True

    def login(self) -> bool:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        hashed_password = self._hash_password(password)

        if username == self.username and hashed_password == self._password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    @property
    def view_profile(self):
        for user in self.users:
            if user.username == self.username:
                return user.profile

    def __str__(self) -> str:
        return (f"Username: {self.username}\nPhone Number: {self.phone_number}\n "
                f" Register on: {self.registration_date}")

    def edit_info(self) -> None:
        new_username = input("Enter a new username: ")
        new_phone_number = input("Enter a new phone number: ")

        if new_username != self.username and new_username in User.users:
            print("Username already taken.")
        else:
            self.username = new_username
            self.phone_number = new_phone_number
            print("Personal information updated successfully.")

    def change_password(self) -> None:
        old_password = getpass.getpass("Enter your old password: ")
        new_password = getpass.getpass("Enter your new password: ")
        confirm_password = getpass.getpass("Confirm your new password: ")

        hashed_old_password = self._hash_password(old_password)

        if hashed_old_password != self._password:
            print("Invalid old password.")
        elif new_password != confirm_password:
            print("New passwords do not match.")
        elif new_password in User.users.values():
            print("Password cannot be repeated.")
        else:
            self._password = self._hash_password(new_password)
            print("Password updated successfully.")

    @staticmethod
    def Birthday_discount(self=None):
        # Get the current date
        current_data = datetime.now().date()
        """از طریق کاربران تکرار کنید و بررسی کنید که آیا تاریخ تولد 
        آنها با تاریخ فعلی مطابقت دارد یا خیر"""
        """# Iterate through the users and check 
        if their birthdate matches the current date"""
        for user in User.users:
            if user.birthday == current_data:
                """#Apply the discount to the user"""
                """تخفیف را برای کاربر اعمال کنید"""
            print(f"Happy birthday : {self.username}!! you get a"
                  f" 50% discount on your next ticket purchase. ")

    def apply_discount(self):
        """Users can get discounts for the number of months they are members"""
        """کاربران به تعداد ماه هایی که عضو هستند میتوانند تخفیف بگیرن"""
        current_date = datetime.now()
        registration_delta = current_date - self.registration_date
        months_as_member = registration_delta.days // 30
        # Apply a maximum 60% discount
        # حداکثر 60 درصد تخفیف اعمال می شود
        discount_percentage = min(months_as_member, 12) * 5
        return discount_percentage

    def is_eligible_for_discount(self):
        """کاربران مجاز به رزرو یا مشاهده فیلمهایی که
         برای رده های سنی بالاتر از او میباشند مجاز نخواهد بود
        """
        # Authorized users will not be allowed to reserve
        # or watch movies that are for older age groups
        if self.age >= 18:
            return True
        else:
            return False

    def watch_movie(self, movie):
        if movie.age_rating > self.age:
            raise Exception("You are not eligible to watch this movie")
