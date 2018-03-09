# -*- coding: utf-8 -*-

"""
twython.compat
~~~~~~~~~~~~~~

This module contains imports and declarations for seamless Python 2 and
Python 3 compatibility.
"""

import sys

_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

try:
    import simplejson as json
except ImportError:
    import json

if is_py2:
    from urllib import urlencode, quote_plus
    from urlparse import parse_qsl, urlsplit

    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)
    def encode_ascii(fun):
        def inner(x):
            return fun(x.encode('ASCII'))
        return inner
    urlsplit = encode_ascii(urlsplit)

    def decode_utf8(fun):
        def inner(x):
            out = fun(x)
            out = [(k, str(v.decode('utf-8'))) for k, v in out]
            return out
        return inner
    parse_qsl = decode_utf8(parse_qsl)

elif is_py3:
    from urllib.parse import urlencode, quote_plus, parse_qsl, urlsplit

    str = str
    basestring = (str, bytes)
    numeric_types = (int, float)
