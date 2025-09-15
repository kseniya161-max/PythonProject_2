import keyword

from src. options import Connect
from src.vacancy import VacancyWorking
from typing import List


def user_interreaction():
    """Функия взаимодействует с пользоателем"""
    api = Connect()
    while True:
        print("\nВыберите действие: ")
        print("1. Введите вакансию")
        print("2. Получите топ N вакансий по зарплате")
        print("3. Получить вакансию с ключевым словом в описании")

        user_choice = input("Выберите номер действия: ")
        if user_choice == "1":
            vacancies_data = api.vacancies(keyword)
            if vacancies_data:
                print(f"Найдено {len("vacancies_data")} по запросу '{keyword}'.")
                for i, data in enumerate(vacancies_data, start = 1):
                    name = data.get("name", "Нет названия")
                    link = data.get("alternate_link", "Нет ссылки")
                    salary_info = data.get('salary')
                    salary = salary_info ["from"] if salary_info and ["from"] in salary_info else 0
                    print(f"{i}.{name} - {salary} - {link}")
            else:
                print("Вакансии не найдены")
        elif user_choice == "2":




