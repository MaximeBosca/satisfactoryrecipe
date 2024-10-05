from satisfactoryrecipe.item import Item


def test_create_item():
    item = Item("Item","")
    assert item is not None


def test_item_equals():
    item = Item("An item", "")
    same_item = Item("An item", "ignored field")
    different_item = Item("Different item", "")
    assert item == same_item
    assert item != different_item


def test_item_hash():
    item = Item("An item", "")
    same_item = Item("An item", "ignored field")
    different_item = Item("Different item", "")
    assert hash(item) == hash(same_item)
    assert hash(item) != hash(different_item)
