import pytest
from src.vacancy import VacancyWorking


def test_vacancy_initialization():
        vacancy = VacancyWorking("Разработчик", "https://example.com/vacancy/1", 200000, "Описание вакансии")
        assert vacancy.name == "Разработчик"
        assert vacancy.link == "https://example.com/vacancy/1"
        assert vacancy.salary == 200000
        assert vacancy.description == "Описание вакансии"


def test_salary_compare():
        vacancy1 = VacancyWorking("Разработчик", "https://example.com/vacancy/1", 200000, "Описание вакансии")
        vacancy2 = VacancyWorking("Тестировщик", "https://example.com/vacancy/2", 150000, "Описание вакансии")
        assert vacancy1 > vacancy2
        assert vacancy2 < vacancy1


def test_salary():
        vacancy = VacancyWorking("Разработчик", "https://example.com/vacancy/1", 200000, "Описание вакансии")
        assert vacancy.salary_compare() == "Заработная плата по  позиции Разработчик составляет: 200000"
        vacancy_zero = VacancyWorking("Разработчик", "https://example.com/vacancy/1", 0, "Описание вакансии")
        assert vacancy_zero.salary_compare() == "Заработная плата ровна 0"
