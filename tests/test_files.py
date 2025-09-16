import pytest
from src.files import Saving
import os


@pytest.fixture
def saving_handler():
    test_filename = "test_vacancies.json"
    if os.path.exists(test_filename):
        os.remove(test_filename)
    handler = Saving(filename=test_filename)
    yield handler
    os.remove(test_filename)


def test_adding(saving_handler):
    """Тестирует добавляет ли вакансии"""
    vacancy_data = {
        "id": "1",
        "name": "Программист",
        "link": "https://example.com/vacancy/1",
        "salary": 50000,
        "description": "С опытом работы"
    }
    saving_handler.add_vacancy(vacancy_data)
    assert len(saving_handler.vacancies) == 1


def test_dublicate(saving_handler):
    """Тетсируется добваляется ли дубликат"""
    vacancy_data = {
        "id": "1",
        "name": "Программист",
        "link": "https://example.com/vacancy/1",
        "salary": 50000,
        "description": "С опытом работы"
    }
    saving_handler.add_vacancy(vacancy_data)
    saving_handler.add_vacancy(vacancy_data)
    assert len(saving_handler.vacancies) == 1

