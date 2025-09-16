import pytest
from unittest.mock import MagicMock
from src.Utils import print_vacancies, get_vacancies, filter_vacancies_by_keyword


def test_get_vacancies():
    mock_api = MagicMock()
    mock_api.vacancies.return_value = [{"id": 1, "name": "Разработчик"}]

    result = get_vacancies(mock_api, "Разработчик")

    assert len(result) == 1
    assert result[0]['name'] == "Разработчик"


def test_filter_vacancies_by_keyword():
    vacancies_data = [
        {
            "snippet": {
                "requirement": "Опыт работы с Python"
            }
        },
        {
            "snippet": {
                "requirement": "Опыт работы с Java"
            }
        }
    ]

    keyword = "Python"
    filtered_vacancies = filter_vacancies_by_keyword(vacancies_data, keyword)

    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0]['snippet']['requirement'] == "Опыт работы с Python"
