import pytest
from src. options import Connect

@pytest.fixture
def api():
    return Connect()


def test_connections(api):
    api._connection()
    assert api._session is not None




