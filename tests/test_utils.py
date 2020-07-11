from utils.utils import get_aware_dt


def test_get_aware_dt():
    assert get_aware_dt().tzinfo is not None
