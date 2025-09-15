from src.options import Connect
from src.files import Saving
from src.vacancy import VacancyWorking
from src.User import user_interreaction
from src.Utils import print_vacancies, get_vacancies, filter_vacancies_by_keyword
import json



def main():
    api = Connect()

    # Получаем вакансии по запросу "разработчик"
    vacancies_data = api.vacancies("разработчик")

    # Проверяем, есть ли вакансии
    vacancies = []  # Инициализация списка для хранения объектов VacancyWorking
    if vacancies_data:
        print("Найденные вакансии:")
        for data in vacancies_data:
            name = data.get('name', 'Нет названия')
            link = data.get('alternate_url', 'Нет ссылки')
            salary_info = data.get('salary')
            salary = salary_info['from'] if salary_info and 'from' in salary_info else 0
            description = data.get('snippet', {}).get('requirement', 'Нет описания')

            vacancy = VacancyWorking(name, link, salary, description)  # Создание объекта VacancyWorking
            vacancies.append(vacancy)  # Добавление объекта в список
            print(f"{vacancy.name} - {vacancy.link} - {vacancy.salary}")
    else:
        print("Вакансии не найдены.")
    vacancies_list = [vacancy.to_dict() for vacancy in vacancies]
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies_list, f, ensure_ascii=False, indent=4)

    print("Данные о вакансиях успешно сохранены в файл vacancies.json.")

    # Создаем экземпляр Saving для работы с Json файлом
    saving_handler = Saving(filename="my_vacancies.json")

    # Добавления вакансии
    vacancy_data = {
        "id": 1,
        "name": "Программист Python",
        "link": "https://example.com/vacancy/1",
        "salary": 80000,
        "description": "Ищем опытного программиста Python."
    }
    saving_handler.add_vacancy(vacancy_data)

    # Удаление вакансии
    saving_handler.delete_vacancy(vacancy_id=1)

    # Вывод текущих вакансий
    print("Текущие вакансии в my_vacancies.json:")
    print(saving_handler.vacancies)

    # Создаем еще один экземпляр Saving для другого файла
    other_saving_handler = Saving(filename="other_vacancies.json")

    # Пример добавления вакансии в другой файл
    other_vacancy_data = {
        "id": 2,
        "name": "Программист Java",
        "link": "https://example.com/vacancy/2",
        "salary": 90000,
        "description": "Ищем опытного программиста Java."
    }
    other_saving_handler.add_vacancy(other_vacancy_data)

    # Вывод текущих вакансий в другом файле
    print("Текущие вакансии в other_vacancies.json:")
    print(other_saving_handler.vacancies)

if __name__ == "__main__":
    main()