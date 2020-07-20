import utils.utils as tgt


def test_get_aware_dt():
    assert tgt.get_aware_dt().tzinfo is not None


def test_pytest_donot_call_method(mocker):

    m = mocker.patch.object(
        tgt,
        '_print_hello',
        return_value=None)

    tgt.pytest_donot_call_method()

    m.assert_called_once_with()
