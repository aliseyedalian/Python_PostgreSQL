from user import User

my_user = User(email="seyedalian@outlook.com",first_name="Ali",last_name="Seyedalian",id = 1)

new_user = User.load_from_db_by_email("seyedalian@outlook.com")

print(new_user)