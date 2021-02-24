# import sys
# sys.path.append('.')
# from project.user import User

class Library:
    '''
        book_available:
            Key Autors, Value: book for this author
        user_records:
            Users objects
        rented_book:
            {username: {book_names: days left}}
    '''
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        if user.username in self.rented_books:
            del self.rented_books[user.username]

    def change_username(self, user_id: int, new_username: str):
        try:
            temp_user = [u for u in self.user_records if u.user_id == user_id][0]
        except IndexError:
            return "There is no user with id = %d!" % user_id
        else:
            if temp_user.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
            temp_user.username = new_username
            return "Username successfully changed to: %s for userid: %d" % (new_username, user_id)
