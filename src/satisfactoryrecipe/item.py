from typing import Optional


class Item:
    def __init__(self, name: str, image_path: Optional[str] = None):
        self.name, self.image_path = name, image_path

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Item : {self.name}"
