from user import User
from database import connection_pool


my_user = User(email="heidari@yahoo.com",first_name="Ali",last_name="Heidari")

my_user.save_to_db()

user = User.get_user_from_db_by_email("kaviani@yahoo.com")

print(user)

