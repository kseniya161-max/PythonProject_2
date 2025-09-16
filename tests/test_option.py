import pytest
from src. options import Connect

@pytest.fixture
def api():
    return Connect()


def test_connections(api):
    api._connection()
    assert api._session is not None


def test_vacancies(api):
    api._connection()
    vacancies = api.vacancies("руководитель")
    assert isinstance (vacancies, list)
    if vacancies:
        assert "name" in vacancies[0]




