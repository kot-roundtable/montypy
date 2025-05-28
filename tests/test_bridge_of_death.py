from montypy.grail import bridge_of_death


def test_airspeed():
    actual = bridge_of_death.airspeed()
    expected = 20.1
    assert actual == expected
