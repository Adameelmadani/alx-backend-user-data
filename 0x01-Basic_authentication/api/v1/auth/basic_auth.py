#!/usr/bin/env python3
"""
This python module contains BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar
"""
Auth class from auth module
base64 module
typing module
"""


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth class
    """
    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """
        function that extract the base64 authorization header
        """
        if auth_header is None:
            return None
        elif not isinstance(auth_header, str):
            return None
        elif not auth_header.startswith("Basic "):
            return None
        return auth_header[6:]

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """
        function that decodes b64 authorization header
        """
        if b64_auth_header is None:
            return None
        elif not isinstance(b64_auth_header, str):
            return None
        try:
            decoded_auth_header = base64.b64decode(b64_auth_header)
            return decoded_auth_header.decode('utf-8')
        except Exception as e:
            return None

    def extract_user_credentials(self, dec_b64_auth_header: str) -> (str, str):
        """
        function that returns user email and password for b64 decoded value
        """
        if dec_b64_auth_header is None:
            return (None, None)
        elif not isinstance(dec_b64_auth_header, str):
            return (None, None)
        elif ":" not in dec_b64_auth_header:
            return (None, None)
        user_inf_list = dec_b64_auth_header.split(":")
        return (user_inf_list[0], user_inf_list[1])

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """
        function that returns user object from email and pwd
        """
        if user_email is None or (not isinstance(user_email, str)):
            return None
        if user_pwd is None or (not isinstance(user_pwd, str)):
            return None
        user_list = User.search({'email': user_email})
        if len(user_list) == 0:
            return None
        for user in user_list:
            if user.is_valid_password(user_pwd) is True:
                return user
        return None
