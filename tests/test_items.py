from json import load

from rl_data_utils.exceptions import InvalidAttribute
from rl_data_utils.item.attribute.attribute import Archived, Certified, Color, Name, Quantity, Rarity, Serie, Slot, \
    Tradable
from rl_data_utils.item.item.constants import INDENTIFIER
from rl_data_utils.item.item.item import Item
from rl_data_utils.items.items import Items

with open("sample-inventory-items.json", "r") as file:
    json = load(file)

items_json = json["items"]
inventory_items = Items()
for item in items_json:
    try:
        item_object = Item(
            color=Color(item["color"]),
            rarity=Rarity(item["rarity"]),
            slot=Slot(item["slot"]),
            certified=Certified(item["certified"]),
            name=Name(item["name"]),
            quantity=Quantity(item["quantity"]),
            tradable=Tradable(item["tradable"]),
            serie=Serie(item["serie"])
        )
    except InvalidAttribute:
        continue
    else:
        inventory_items.add_items(item_object)


def test_filter_by_item_indentifier_mode():
    item_ = Item(Archived(True), Name("Dingo"), Slot("Car"), Color("Saffron"), Rarity("Import"),
                 Certified("GoalKeeper"), Quantity(6))
    i = inventory_items.filter_by_item(item_, INDENTIFIER)
    print(i.items)


def test_filter_by():
    i = inventory_items.filter_by_item(Item(name=Name("Octane: Buzz Kill")))
    print(i.items)


def test_filter_by_item():
    item_ = Item(name=Name("Octane: Buzz Kill"))
    print(inventory_items.filter_by_item(item_).items)
