def id():
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    import random
    return "#" + (''.join(random.choice(string) for _ in range(5)))


def test_id():
    """Test the id function."""
    result = id()
    assert len(result) == 6, "ID should be 10 characters long"
    assert all(
        c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for c in result[1:]), "ID should only contain alphanumeric characters"
    print("Test passed!")


print(id())
test_id()