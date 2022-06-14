import pickle
from os.path import join, exists

class Bank:
    def __init__(self, name):
        self._name = name
        if exists(self.storage_location):
            self.load()
        else:
            self.save()
    
    @property
    def name(self):
        return self._name

    @property
    def storage_location(self):
        return join("data", "banks", f"{self.name}.pickle")

    def save(self):
        with open(self.storage_location, "wb") as f:
            pickle.dump(self.__dict__, f)

    def load(self):
        with open(self.storage_location, "rb") as f:
            self.__dict__ = pickle.load(f)