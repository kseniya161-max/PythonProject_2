from src.options import Connect
from src.files import Saving
from src.vacancy import VacancyWorking
from src.User import user_interreaction
from src.Utils import print_vacancies, get_vacancies, filter_vacancies_by_keyword
import json

def main():
    api = Connect()
    saving_handler = Saving(filename="my_vacancies.json")
    user_interreaction(api, saving_handler)

    # Создание первой вакансии
    vacancy1 = VacancyWorking(
        name="Программист Python",
        link="https://example.com/vacancy/1",
        salary=80000,
        description="Ищем опытного программиста Python."
    )

    # Добавление первой вакансии в файл
    saving_handler.add_vacancy(vacancy1.to_dict())

    # Создание второй вакансии
    vacancy2 = VacancyWorking(
        name="Программист Java",
        link="https://example.com/vacancy/2",
        salary=90000,
        description="Ищем опытного программиста Java."
    )

    # Добавление второй вакансии в другой файл
    other_saving_handler = Saving(filename="other_vacancies.json")
    other_saving_handler.add_vacancy(vacancy2.to_dict())

    # Сравнение зарплат
    if vacancy2 > vacancy1:
        print(f"{vacancy2.name} имеет более высокую зарплату, чем {vacancy1.name}")
    else:
        print(f"{vacancy1.name} имеет более высокую зарплату, чем {vacancy2.name}")

    # Вывод текущих вакансий в my_vacancies.json
    print("Текущие вакансии в my_vacancies.json:")
    print(saving_handler.vacancies)

    # Вывод текущих вакансий в other_vacancies.json
    print("Текущие вакансии в other_vacancies.json:")
    print(other_saving_handler.vacancies)


if __name__ == "__main__":
    main()

