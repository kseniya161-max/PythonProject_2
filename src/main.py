from src.options import Connect
from src.files import Saving
from src.vacancy import VacancyWorking
from src.User import user_interreaction
from src.Utils import print_vacancies, get_vacancies, filter_vacancies_by_keyword
import json

def main():
    api = Connect()
    saving_handler = Saving(filename="my_vacancies.json")
    user_interreaction()

    vacancy = VacancyWorking(
        name="Программист Python",
        link="https://example.com/vacancy/1",
        salary=80000,
        description="Ищем опытного программиста Python."
    )

    # Добавление вакансии в файл
    saving_handler.add_vacancy(vacancy.to_dict())

    # Удаление вакансии (если необходимо)
    saving_handler.delete_vacancy(vacancy_id=1)

    # Вывод текущих вакансий
    print("Текущие вакансии в my_vacancies.json:")
    print(saving_handler.vacancies)

    # Создаем еще один экземпляр Saving для другого файла
    other_saving_handler = Saving(filename="other_vacancies.json")

    # Создание другой вакансии и добавление ее в другой файл
    other_vacancy = VacancyWorking(
        name="Программист Java",
        link="https://example.com/vacancy/2",
        salary=90000,
        description="Ищем опытного программиста Java."
    )
    other_saving_handler.add_vacancy(other_vacancy.to_dict())

    # Вывод текущих вакансий в другом файле
    print("Текущие вакансии в other_vacancies.json:")
    print(other_saving_handler.vacancies)

if __name__ == "__main__":
    main()