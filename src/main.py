from src. options import Connect


if __name__ == "__main__":
    api = Connect()
    vacancies = api.vacancies("разработчик")
    for vacancy in vacancies:
        print(vacancy['name'], vacancy['url'])

        # Создаем экземпляр Saving для другого файла
        saving_handler = Saving(filename="my_vacancies.json")

        # Добавляем вакансии
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

        # Текущие вакансии
        print(saving_handler.vacancies)

        # Создаем еще один
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

        # Текущие вакансии
        print(other_saving_handler.vacancies)
