# -*- coding: utf-8 -*-
import base64

from flask import request
from flask_apscheduler_plus.utils import bytes_to_wsgi, wsgi_to_bytes


def get_authorization_header():
    """
    Return request's 'Authorization:' header as
    a two-tuple of (type, info).
    """
    header = request.environ.get('HTTP_AUTHORIZATION')

    if not header:
        return None

    header = wsgi_to_bytes(header)

    try:
        auth_type, auth_info = header.split(None, 1)
        auth_type = auth_type.lower()
    except ValueError:
        return None

    return auth_type, auth_info


class Authorization(dict):
    """
    A class to hold the authorization data.

    :param str auth_type: The authorization type. e.g: basic, bearer.
    """

    def __init__(self, auth_type, **kwargs):
        super(Authorization, self).__init__(**kwargs)

        self.auth_type = auth_type


class HTTPAuth(object):
    """
    A base class from which all authentication classes should inherit.
    """

    def get_authorization(self):
        """
        Get the authorization header.
        :return Authentication: The authentication data or None if it is not present or invalid.
        """
        raise NotImplemented()

    def get_authenticate_header(self):
        """
        Return the value of `WWW-Authenticate` header in a
        `401 Unauthenticated` response.
        """
        pass


class HTTPBasicAuth(HTTPAuth):
    """
    HTTP Basic authentication.
    """
    www_authenticate_realm = 'Authentication Required'

    def get_authorization(self):
        """
        Get the username and password for Basic authentication header.
        :return Authentication: The authentication data or None if it is not present or invalid.
        """
        auth = get_authorization_header()

        if not auth:
            return None

        auth_type, auth_info = auth

        if auth_type != b'basic':
            return None

        try:
            username, password = base64.b64decode(auth_info).split(b':', 1)
        except Exception:
            return None

        return Authorization('basic', username=bytes_to_wsgi(username), password=bytes_to_wsgi(password))

    def get_authenticate_header(self):
        """
        Return the value of `WWW-Authenticate` header in a
        `401 Unauthenticated` response.
        """
        return 'Basic realm="%s"' % self.www_authenticate_realm
