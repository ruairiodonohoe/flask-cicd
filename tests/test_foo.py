from flask_cicd.foo import foo


def test_foo():
    assert foo("foo") == "foo"
