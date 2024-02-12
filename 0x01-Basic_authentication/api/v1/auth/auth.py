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
        require_auth function to check if path is in the require_auth paths
        """
        if path is None:
            return True
        elif excluded_paths is None:
            return True
        elif len(excluded_paths) == 0:
            return True
        for e_path in excluded_paths:
            if path == e_path or path == e_path[:-1]:
                return False
        return True


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
