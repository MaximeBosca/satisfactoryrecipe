from src.satisfactoryrecipe.recipe import Recipe
from src.satisfactoryrecipe.item import Item


def test_create_recipe():
    recipe = Recipe("recipe", None, 5)
    assert recipe is not None


def test_add_input():
    recipe = Recipe("recipe", None, 6)
    some_item = Item("some  item", "")
    recipe.add_input(some_item, 1.0)
    assert len(recipe.inputs) == 1
    assert len(recipe.outputs) == 0
    assert recipe.inputs[0].item == some_item
    assert recipe.inputs[0].quantity == 1.0


def test_add_output():
    recipe = Recipe("recipe", None, 6)
    some_item = Item("some  item", "")
    recipe.add_output(some_item, 1.0)
    assert len(recipe.inputs) == 0
    assert len(recipe.outputs) == 1
    assert recipe.outputs[0].item == some_item
    assert recipe.outputs[0].quantity == 1.0
