class CatalogError(Exception):
    pass

class RoomError(CatalogError):
    pass

class DupError(CatalogError):
    pass

class NoRoomError(CatalogError):
    pass

class FormatError(CatalogError):
    pass

class FileError(CatalogError):
    pass
