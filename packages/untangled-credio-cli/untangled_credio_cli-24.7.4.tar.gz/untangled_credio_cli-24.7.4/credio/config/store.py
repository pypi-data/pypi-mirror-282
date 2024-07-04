import os
from typing import Optional, Type, TypeVar


V = TypeVar("V")


class Store(dict):
    def __init__(self):
        pass

    def get(self, key: str, type: Type[V] = str) -> Optional[V]:
        if key in self.keys():
            return self[key]

    def load(self, *keys: str):
        for key in keys:
            self[key] = os.environ[key]
        return self

    def load_all(self):
        return self.load(*os.environ.keys())


default = Store().load_all()
"""Default Configuration Store."""
