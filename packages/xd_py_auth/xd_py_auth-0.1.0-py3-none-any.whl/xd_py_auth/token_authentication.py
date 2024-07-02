from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

load_dotenv()


class JWTConfig:
    TYPES = {
        'ACCESS': 'access',
        'REFRESH': 'refresh'
    }


class TokenAuthentication:

    def __init__(self, access_token_expiry_time='2d',
                 refresh_token_expiry_time='7d',
                 algorithm='HS256',
                 jwt_secret=''):

        jwt_secret = jwt_secret if jwt_secret else os.getenv(
            "JWT_SECRET_KEY", "secret1")

        self.options = {
            'access_token_expiry_time':
            self.parse_expiry_time(access_token_expiry_time),
            'refresh_token_expiry_time':
            self.parse_expiry_time(refresh_token_expiry_time),
            'algorithm': algorithm,
            'jwt_secret': jwt_secret
        }

    @staticmethod
    def parse_expiry_time(expiry_time):
        unit = expiry_time[-1]
        value = int(expiry_time[:-1])
        if unit == 'd':
            return timedelta(days=value)
        elif unit == 'h':
            return timedelta(hours=value)
        elif unit == 'm':
            return timedelta(minutes=value)
        else:
            raise ValueError(f"Unsupported expiry time unit: {unit}")

    def generate_token(self, payload, token_type=JWTConfig.TYPES['REFRESH']):

        secret = self.options['jwt_secret']
        expiry_time = self.options[
            'access_token_expiry_time'] if token_type == JWTConfig.TYPES[
            'ACCESS'] else self.options['refresh_token_expiry_time']
        expiration = datetime.now(timezone.utc) + expiry_time

        token = jwt.encode({'exp': expiration, **payload},
                           secret,
                           algorithm=self.options['algorithm'])
        return token

    def verify_token(self, token: str):

        if not token:
            return {
                'verified': False,
                'payload': None,
            }

        try:
            payload = jwt.decode(token,
                                 self.options['jwt_secret'],
                                 algorithms=[
                                     self.options['algorithm']]
                                 )
            if not payload:
                return {
                    'verified': False,
                    'payload': None,
                }
            return {
                'verified': True,
                'payload': payload,
            }
        except JWTError as e:
            raise JWTError(f"Token verification failed: {e}")
