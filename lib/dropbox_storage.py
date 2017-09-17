from django.utils.deconstruct import deconstructible
from django.core.files.storage import Storage, File
from django.conf import settings

@deconstructible
class DropboxStorage(Storage):

    def __init__(self, option=None):
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS

    def _save(self, name, content):
        pass

    def _open(self, name, mode='rb'):
        pass

    def delete(self, name):
        pass

    def exists(self, name):
        pass

    def url(self, name):
        pass