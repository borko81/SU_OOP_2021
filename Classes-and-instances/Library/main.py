from polymorhism.project import User
from polymorhism.project import Library


user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})


user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)


'''
User with id = 12 already registered in the library!
We could not find such user to remove!
There is no user with id = 2!
Please check again the provided username - it should be different than the username used so far!
Username successfully changed to: George for userid: 12
12, George, []
{'J.K.Rowling': ['The Chamber of Secrets', 'The Prisoner of Azkaban', 'The Goblet of Fire', 'The Order of the Phoenix', 'The Half-Blood Prince']}
{'George': {'The Deathly Hallows': 17}}
['The Deathly Hallows']
The book "The Deathly Hallows" is already rented and will be available in 17 days!
George doesn't have this book in his/her records!
{'J.K.Rowling': ['The Chamber of Secrets', 'The Prisoner of Azkaban', 'The Goblet of Fire', 'The Order of the Phoenix', 'The Half-Blood Prince', 'The Deathly Hallows']}
{'George': {}}
[]
'''
