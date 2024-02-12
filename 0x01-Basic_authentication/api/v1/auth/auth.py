#!/usr/bin/env python3
"""
This module contains the Auth class for authentication
"""
from flask import request
from typing import List, TypeVar
"""
request from flask module
typing module
"""


class Auth:
    """
    Auth class for authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth function to check for authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization_header function to return the author header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user function to return the current_user
        """
        return None
