'''
now we are making appropriate changes in this file after modifications done in user class for database access

'''
'''
this secuirty is actually using helper 'user' class and note the resource user class
'''

from models.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username,password):
    user=UserModel.findByUsername(username)
    if user and safe_str_cmp(user.password,password): # if user and user.password==password:
        return user
def identity(payload):
    user_id=payload['identity']
    return UserModel.findByUseId(user_id)