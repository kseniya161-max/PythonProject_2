import unittest.mock
import pytest
from unittest.mock import MagicMock,patch
from src.User import user_interreaction


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.vacancies.return_value = [{"id": 1,
                                   "name": "Разработчик",
                                   "alternate_url": "https://example.com/vacancy/1",
                                   "salary": {"from": 200000},
                                   "snippet": {"responsibility": "Управление проектами"}


    }]
    return api


def test_user_interreaction_search_vacancy(mock_api, capsys):
    inputs = iter(["1", "Разработчик", "4"])
    with unittest.mock.patch('builtins.input', lambda _: next(inputs)):
        user_interreaction(mock_api, None)


    captured = capsys.readouterr()
    assert "Найдено 1 по запросу 'Разработчик'." in captured.out
    assert "Разработчик" in captured.out
    assert "https://example.com/vacancy/1" in captured.out