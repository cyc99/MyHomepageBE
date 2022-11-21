from .models import User
import bcrypt
import jwt
from my_settings import SECRET_KEY

class TokenManager:
    
    @classmethod
    def generate_token(cls, user):
        user_id = user if type(user) == int else user.id
        user_data = {'user_id': user_id}
        token = jwt.encode(user_data, SECRET_KEY, 'HS256')
        return token
    
    @classmethod
    def decode(cls, token=None, header=None):
        try:
            if not token and header:
                token = header['Authorization'].split(' ')[1]
            data = jwt.decode(token, SECRET_KEY, 'HS256')
            return data['user_id']
        except:
            return None
    
    @classmethod
    def authenticate(cls, id, token=None, header=None):
        try:
            user_id = cls.decode(token, header)
            return id == user_id
        except:
            return False
        
    @classmethod    
    def get_and_auth_user(cls, id, token=None, header=None):
        try:
            if cls.authenticate(id, token, header):
                return User.objects.get(id=id)
        except:
            return None
        
    @classmethod
    def get_user(cls, token=None, header=None):
        try:
            user_id = cls.decode(token, header)
            if user_id:
                return User.objects.get(id=user_id)
            return None
        except:
            return None

