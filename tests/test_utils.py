from montypy.utils import bucket, sword


def test_sword():
    actual = sword()
    expected = "sword"
    assert actual == expected


def test_bucket():
    actual = bucket()
    expected = "bucket"
    assert actual == expected
