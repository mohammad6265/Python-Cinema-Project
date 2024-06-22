from user import User


def home(view_profile=None):
    user = None

    while True:
        choice = input("Enter 0 to exit,\n 1 to register a new user,\n 2 to login,"
                       "\n or 3 to continue as a logged-in user: ")

        if choice == "0":
            print("Program ended.")
            break
        elif choice == "1":
            User.register_user()
        elif choice == "2":
            username = input("Enter your username: ")
            if username in User.users:
                user = User.users[username]
                if user.login():
                    break
            else:
                print("Invalid username.")
        elif choice == "3" and user is not None:
            while True:
                choice_logged_in = input(
                    "Enter 1 to print user information,"
                    " 2 to edit personal information,"
                    " 3 to change password, or 4 to logout: ")

                if choice_logged_in == "1":
                    print(user)
                    print(view_profile)
                    
                elif choice_logged_in == "2":
                    user.edit_info()
                elif choice_logged_in == "3":
                    user.change_password()
                elif choice_logged_in == "4":
                    user = None
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Invalid choice.")


home()
