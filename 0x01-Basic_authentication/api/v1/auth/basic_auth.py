#!/usr/bin/env python3
"""
This python module contains BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64
"""
Auth class from auth module
base64 module
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
