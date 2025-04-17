import os


class StorageBase:

    storagePath: str = "./data"

    def Load(self):
        pass

    def Store(self):
        pass

    def TryMakeStorageDirectory(self):
        if not os.path.exists(self.storagePath):
            os.mkdir(self.storagePath)
