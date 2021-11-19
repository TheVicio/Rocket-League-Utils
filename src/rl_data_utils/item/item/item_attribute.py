from contextlib import suppress
from rl_data_utils.item.blueprint.abc_base_blueprint import ABCBaseBlueprint
from rl_data_utils.item.color.abc_base_color import ABCBaseColor
from rl_data_utils.item.paintable.abc_base_paintable import ABCBasePaintable
from rl_data_utils.item.price.abc_base_price import ABCBasePrice
from rl_data_utils.item.serie.abc_base_serie import ABCBaseSerie
from rl_data_utils.item.tradable.abc_base_tradable import ABCBaseTradable
from rl_data_utils.item.type.abc_base_type import ABCBaseType
from rl_data_utils.item.rarity.abc_base_rarity import ABCBaseRarity
from rl_data_utils.item.certified.abc_base_certified import ABCBaseCertified
from rl_data_utils.item.quantity.abc_base_quantity import ABCBaseQuantity
from rl_data_utils.item.name.abc_base_name import ABCBaseName
from rl_data_utils.utils.item_attributes.item_attributes import get_repr


class ItemAttribute:
    def validate(self):
        if isinstance(self, ABCBaseColor):
            self.validate_color()
        if isinstance(self, ABCBaseRarity):
            self.validate_rarity()
        if isinstance(self, ABCBaseType):
            self.validate_type()
        if isinstance(self, ABCBaseCertified):
            self.validate_certified()

    def __eq__(self, other):
        return self.compare_items(other)

    def __repr__(self):
        return get_repr(**self.item_attributes_to_dict())

    def is_valid(self) -> bool:
        if isinstance(self, ABCBaseColor):
            is_valid = self.is_valid_color()
            if not is_valid:
                return False
        if isinstance(self, ABCBaseRarity):
            is_valid = self.is_valid_rarity()
            if not is_valid:
                return False
        if isinstance(self, ABCBaseType):
            is_valid = self.is_valid_type()
            if not is_valid:
                return False
        if isinstance(self, ABCBaseCertified):
            is_valid = self.is_valid_certified()
            if not is_valid:
                return False
        if isinstance(self, ABCBaseSerie):
            is_valid = self.is_valid_serie()
            if not is_valid:
                return False
        return True

    def compare_items(self, item):
        if isinstance(self, ABCBaseColor) and isinstance(item, ABCBaseColor):
            cc = self.compare_colors(item.get_color())
            if not cc:
                return False
        if isinstance(self, ABCBaseRarity) and isinstance(item, ABCBaseRarity):
            rc = self.compare_rarities(item.get_rarity())
            if not rc:
                return False
        if isinstance(self, ABCBaseType) and isinstance(item, ABCBaseType):
            tc = self.compare_types(item.get_type())
            if not tc:
                return False
        if isinstance(self, ABCBaseCertified) and isinstance(item, ABCBaseCertified):
            cc = self.compare_certificates(item.get_certified())
            if not cc:
                return False
        if isinstance(self, ABCBaseName) and isinstance(item, ABCBaseName):
            cn = self.compare_name(item.get_name())
            if not cn:
                return False
        return True

    def item_attributes_to_dict(self) -> dict:
        attrs = {}
        if isinstance(self, ABCBaseColor):
            color = self.get_color()
            if color:
                attrs['color'] = color
        if isinstance(self, ABCBaseRarity):
            rarity = self.get_rarity()
            if rarity:
                attrs['rarity'] = rarity
        if isinstance(self, ABCBaseType):
            type_ = self.get_type()
            if type_:
                attrs['type_'] = type_
        if isinstance(self, ABCBaseCertified):
            certified = self.get_certified()
            if certified:
                attrs['certified'] = certified
        if isinstance(self, ABCBaseName):
            name = self.get_name()
            if name:
                attrs['name'] = name
        if isinstance(self, ABCBaseQuantity):
            attrs['quantity'] = self.get_quantity()
        if isinstance(self, ABCBaseTradable):
            attrs['tradable'] = self.get_tradable()
        if isinstance(self, ABCBasePaintable):
            attrs['paintable'] = self.get_paintable()
        if isinstance(self, ABCBaseSerie):
            serie = self.get_serie()
            if serie:
                attrs['serie'] = serie
        if isinstance(self, ABCBaseBlueprint):
            attrs['blueprint'] = self.get_blueprint()
        return attrs

