# Exercise Dictionary Methods
# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {'age':0, 'username' : ' ','weapons': ' ','is_activate': False,'clan': None}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())
# 3 Add a new weapon to your user
user_profile['weapons'] = 'Spear'
# 4 Add a new key to include 'is_banned'. Set it to false
user_profile['is_banned'] = False
# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True
# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'age':24,'username':'Luffy'})
