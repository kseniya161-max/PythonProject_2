import pytest
from src.vacancy import VacancyWorking


def test_vacancy_initialization():
        vacancy = VacancyWorking("Разработчик", "https://example.com/vacancy/1", 200000, "Описание вакансии")
        assert vacancy.name == "Разработчик"
        assert vacancy.link == "https://example.com/vacancy/1"
        assert vacancy.salary == 200000
        assert vacancy.description == "Описание вакансии"

