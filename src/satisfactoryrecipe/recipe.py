from .machine import Machine
from .item import Item
from typing import List, Optional


class RecipeComponent:
    def __init__(self, item: Item, quantity: float):
        self.item = item
        self.quantity = quantity

    def __repr__(self):
        return f"{self.quantity} x {self.item}"


class Recipe:
    inputs: List[RecipeComponent]
    outputs: List[RecipeComponent]

    def __init__(self, name: str, machine: Optional[Machine] = None, crafting_time: Optional[float] = None):
        self.name, self.machine, self.crafting_time = name, machine, crafting_time
        self.inputs, self.outputs = [], []

    def add_input(self, item: Item, quantity: float):
        self.inputs.append(RecipeComponent(item=item, quantity=quantity))

    def add_output(self, item: Item, quantity: float):
        self.outputs.append(RecipeComponent(item=item, quantity=quantity))

    def __repr__(self):
        return (f"{self.name} : {self.machine} ({self.crafting_time}s), "
                f"Inputs : {self.inputs}, "
                f"Outputs : {self.outputs} ")
