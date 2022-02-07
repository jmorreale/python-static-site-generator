import re
from abc import ABC

from yaml import load, FullLoader
from _collections_abc import Mapping


class Content(Mapping, ABC):
    __delimeter = '^(?:-|\+){3}\s*$'
