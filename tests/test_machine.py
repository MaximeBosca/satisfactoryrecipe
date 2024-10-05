from satisfactory_recipe.machine import Machine


def test_create_machine():
    machine = Machine("machine","")
    assert machine is not None


def test_machine_equals():
    machine = Machine("A machine", "")
    same_machine = Machine("A machine", "ignored field")
    different_machine = Machine("Different machine", "")
    assert machine == same_machine
    assert machine != different_machine


def test_machine_hash():
    machine = Machine("A machine", "")
    same_machine = Machine("A machine", "ignored field")
    different_machine = Machine("Different machine", "")
    assert hash(machine) == hash(same_machine)
    assert hash(machine) != hash(different_machine)