#!/usr/bin/env python3
"""
This python module contains BasicAuth class
"""
from api.v1.auth.auth import Auth
"""
Auth class from auth module
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
