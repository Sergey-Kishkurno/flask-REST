from werkzeug.security import safe_str_cmp
from core.models.user import UserModel

# users = [
#     User(1, 'bob', 'asdf')
# ]
# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}
# After we have added methods for finding to User class - there is no need for these mappings so far.

def authenticate(username, password):
    print ("autenticate() called!!!")
    user = UserModel.find_by_username(username)
    # print (user)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    print ("identity() called!!!")
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

