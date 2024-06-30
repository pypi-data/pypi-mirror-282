def test_version():
    from mothra.__about__ import __version__

    assert __version__.count(".") == 2
