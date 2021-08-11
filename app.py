from user import User
from database import Database

my_user = User(email="aheidari@yahoo.com",first_name="Ali",last_name="Heidari")

Database.initialize()
my_user.save_to_db()

user = User.get_user_from_db_by_email("kaviani@yahoo.com")

print(user.last_name)

