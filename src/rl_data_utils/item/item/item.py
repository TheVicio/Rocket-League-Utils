from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string
from rl_data_utils.item.name.name import ABCName
from rl_data_utils.item.color.color import ABCColor
from rl_data_utils.item.type.type import ABCType
from rl_data_utils.item.rarity.rarity import ABCRarity
from rl_data_utils.item.certified.certified import ABCCertified
from rl_data_utils.item.quantity.quantity import ABCQuantity


class Item(ABCName, ABCColor, ABCType, ABCRarity, ABCCertified, ABCQuantity):
    def __init__(self, name: str, color: str = "", type_: str = "", rarity: str = "", certified: str = "",
                 quantity: int = 1):
        self.name = name
        self.color = color
        self.type = type_
        self.rarity = rarity
        self.certified = certified
        self.quantity = quantity

    def get_certified(self):
        return self.certified

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity

    def get_type(self):
        return self.type

    def get_quantity(self) -> int:
        return self.quantity

    @staticmethod
    def from_string(string: str):
        return Item(**get_attributes_in_string(string))
