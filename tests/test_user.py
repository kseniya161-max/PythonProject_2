import pytest
from unittest.mock import MagicMock, patch
from src.User import user_interreaction
from src.Utils import print_vacancies


@pytest.fixture
def mock_api():
    api = MagicMock()
    api.vacancies.return_value = [
        {
            "id": 1,
            "name": "Разработчик",
            "link": "https://example.com/vacancy/1",
            "salary": {"from": 200000},
            "snippet": {"responsibility": "Управление проектами"}
        }
    ]
    return api

def test_user_interreaction_search_vacancy(mock_api, capsys):
    inputs = iter(["1", "Разработчик", "4"])
    with patch('builtins.input', lambda _: next(inputs)):
        user_interreaction(mock_api, None)

    captured = capsys.readouterr()
    assert "Найдено 1 по запросу 'Разработчик'." in captured.out
    assert "Разработчик" in captured.out
    assert "https://example.com/vacancy/1" in captured.out


def test_print_vacancies(capsys):
    vacancies_data = [
        {
            "name": "Разработчик",
            "link": "https://example.com/vacancy/1",
            "salary": {"from": 100000}
        },
        {
            "name": "Тестировщик",
            "link": "https://example.com/vacancy/2",
            "salary": {"from": 80000}
        }
    ]

    print_vacancies(vacancies_data)

    captured = capsys.readouterr()
    assert "1.Разработчик - 100000 - https://example.com/vacancy/1" in captured.out
    assert "2.Тестировщик - 80000 - https://example.com/vacancy/2" in captured.out





