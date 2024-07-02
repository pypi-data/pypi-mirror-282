from abc import abstractmethod
from datetime import date

from .our_object import OurObject
from .temp import deprecation_warning


class Item(OurObject):
    def __init__(self, **kwargs):
        deprecation_warning("item", "DELETE", date(2024, 6, 5))
        super().__init__(**kwargs)

    @abstractmethod
    def get_id(self):
        raise NotImplementedError("Subclasses must implement the 'get_id' method.")
