from .machine import Machine
from .item import Item
from typing import List, Optional


class RecipeItem:
    def __init__(self, item: Item, quantity: int, crafting_time: int):
        self.item = item
        self.quantity = quantity
        self.quantity_per_minute = (60/crafting_time)*quantity if crafting_time > 0 else 0


class Recipe:
    inputs: List[RecipeItem]
    outputs: List[RecipeItem]

    def __init__(self, name: str, machine: Optional[Machine] = None, crafting_time: Optional[int] = None):
        self.name, self.machine, self.crafting_time = name, machine, crafting_time
        self.inputs, self.outputs = [], []

    def add_input(self, item: Item, quantity: int):
        self.inputs.append(RecipeItem(item=item, quantity=quantity, crafting_time=self.crafting_time))

    def add_output(self, item: Item, quantity: int):
        self.outputs.append(RecipeItem(item=item, quantity=quantity, crafting_time=self.crafting_time))

    def __repr__(self):
        return f"Recipe : {self.name}"
