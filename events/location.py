from abc import ABC, abstractmethod


class Location(ABC):
    @abstractmethod
    def as_dict(self) -> dict:
        pass
