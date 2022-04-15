import unittest


class Item:
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name

    def __str__(self):
        return f"#{self.id} {self.name}"

    def __repr__(self):
        return self.__str__()


class Warehouse:
    def __init__(self, capacity=None):
        self._items = []
        self.capacity = capacity

    def stock(self, item: Item):
        if item.id in [i.id for i in self._items]:
            return False

        if self.capacity and len(self._items) >= self.capacity:
            return False

        self._items.append(item)
        return True

    def count(self, item_name: str):
        return len([1 for x in self._items if x.name == item_name])
        # return len(list(filter(lambda x: x.name == item_name, self._items)))

    def unstock_id(self, id: int):
        found_item = None
        for item in self._items:
            if item.id == id:
                found_item = item
                self._items.remove(found_item)
                break

        return found_item

    def unstock_name(self, item_name: str):
        found_items = []
        for item in self._items:
            if item.name == item_name:
                found_items.append(item)
                self._items.remove(item)

        return found_items

    def inventory(self):
        inventory = {}
        for item in self._items:
            if item.name in inventory:
                inventory[item.name] += 1
            else:
                inventory[item.name] = 1

        return inventory

    def item_names(self):
        return [item.name for item in self._items]


class WarehouseTestCase(unittest.TestCase):
    def setUp(self):
        self.wh = Warehouse()
        self.item = Item(1, "Sroubovak")
        self.wh_with_item = Warehouse()
        self.wh_with_item.stock(self.item)

    def test_stock_item(self):
        result = self.wh.stock(self.item)
        self.assertTrue(result)
        self.assertIn(self.item, self.wh._items)

    def test_stock_item_non_unique_duplicate(self):
        self.wh.stock(self.item)
        result = self.wh.stock(self.item)
        self.assertFalse(result)
        self.assertEquals(1, len(self.wh._items))

    def test_stock_item_non_unique_different_id(self):
        self.wh.stock(Item(1, "Vrtacka"))
        result = self.wh.stock(self.item)
        self.assertFalse(result)
        self.assertEquals(1, len(self.wh._items))

    def test_stock_item_full_capacity(self):
        wh = Warehouse(capacity=1)
        wh.stock(self.item)
        result = wh.stock(Item(2, "Vrtacka"))
        self.assertFalse(result)
        self.assertEquals(1, len(wh._items))

    def test_unstock_by_id(self):
        self.assertEqual(self.wh_with_item.unstock_id(self.item.id), self.item)
        self.assertEqual(self.wh_with_item._items, [])

    def test_unstock_by_name(self):
        self.assertEqual(self.wh_with_item.unstock_name(self.item.name), [self.item])
        self.assertEqual(self.wh_with_item._items, [])

    def test_unstock_by_name_not_found(self):
        self.assertEqual(self.wh.unstock_name(self.item.name), [])

    def test_unstock_by_id_not_found(self):
        self.assertEqual(self.wh.unstock_id(self.item.id), None)

    def test_inventory(self):
        self.assertEqual(self.wh_with_item.inventory(), {"Sroubovak": 1})

    def test_inventory_empty(self):
        self.assertEqual(self.wh.inventory(), {})

    def test_item_names(self):
        self.assertEqual(self.wh_with_item.item_names(), ["Sroubovak"])

    def test_item_names_empty(self):
        self.assertEqual(self.wh.item_names(), [])