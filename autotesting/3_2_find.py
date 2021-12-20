def test_substring(full_string, substring):
    assert substring == full_string[full_string.find(substring):(full_string.find(substring)+len(substring))],\
        f"expected '{substring}' to be substring of '{full_string}'"


test_substring('fulltext', 'some_value')
