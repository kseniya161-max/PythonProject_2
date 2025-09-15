import keyword

from src.options import Connect
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
        print("4. Выход")

        user_choice = input("Выберите номер действия: ")
        if user_choice == "1":
            keyword = input("Введите поисковые запросы: ")
            vacancies_data = api.vacancies(keyword)
            if vacancies_data:
                print(f"Найдено {len(vacancies_data)} по запросу '{keyword}'.")
                for i, data in enumerate(vacancies_data, start = 1):
                    name = data.get("name", "Нет названия")
                    link = data.get("alternate_link", "Нет ссылки")
                    salary_info = data.get('salary')
                    salary = salary_info ["from"] if salary_info and "from" in salary_info else 0
                    print(f"{i}.{name} - {salary} - {link}")
            else:
                print("Вакансии не найдены")
        elif user_choice == "2":
            n = int(input("Введите количество вакансий: "))
            keyword = input ("Введите поисковой запрос: ")
            vacancies_data = api.vacancies(keyword)
            sorted_vacancies = sorted(
                vacancies_data,
                key=lambda x: x.get('salary', {}).get('from', 0) if x.get('salary') is not None else 0,
                reverse=True
            )[:n]
            if sorted_vacancies:
                for i, data in enumerate(sorted_vacancies, start = 1):
                    name = data.get("name", "Нет названия")
                    link = data.get("alternate_link", "Нет ссылки")
                    salary_info = data.get('salary')
                    salary = salary_info["from"] if salary_info and "from" in salary_info else 0
                    print(f"{i}. {name} - {salary} - {link}")
                else:
                    print("Вакансии не найдены.")
        elif user_choice == "3":
            keyword = input("Введите ключевое слово для поиска в описании: ")
            vacancies_data = api.vacancies(keyword)
            filtered_vacancies = [
                data for data in vacancies_data
                if data.get('snippet') and
                   data['snippet'].get('requirement') and
                   keyword.lower() in data['snippet']['requirement'].lower()
            ]

            if filtered_vacancies:
                for i, data in enumerate(filtered_vacancies, start=1):
                    name = data.get("name", "Нет названия")
                    link = data.get("alternate_url", "Нет ссылки")
                    salary_info = data.get('salary')
                    salary = salary_info["from"] if salary_info and "from" in salary_info else 0
                    print(f"{i}. {name} - {salary} - {link}")
            else:
                print("Вакансии не найдены.")
        elif user_choice == "4":
            print("Выход из программы")
            break
        else:
            print ("Неверный ввод. Выберите действие")


if __name__ == "__main__":
    user_interreaction()








