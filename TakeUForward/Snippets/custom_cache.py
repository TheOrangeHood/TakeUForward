from django.core.cache import caches
from django.core.cache.backends.base import BaseCache
from django.utils.connection import ConnectionProxy

Default_Timeout = 300  # in seconds


class CustomCache(BaseCache):
    def __init__(self):
        try:
            self.cache = ConnectionProxy(caches, "default")
        except Exception as e:
            self.cache = None

    def get(self, key, default=None):
        try:
            return self.cache.get(key)
        except Exception as exc:
            return default

    def set(self, key, value, timeout=Default_Timeout):
        try:
            return self.cache.set(key, value, timeout)
        except Exception as exc:
            return False

    def delete(self, key: str):
        try:
            return self.cache.delete(key)
        except Exception as exc:
            return False


custom_cache = CustomCache()
