import pytest

from generators import ari_prog


def test_ari_prog():
    generator = ari_prog(0, 10, 2)
    expected_results = [0, 2, 4, 6, 8]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)
