from database import *

if __name__ == '__main__':
    print(__name__)
    a = user_db.UserDB()
    print(a.show_tables())

