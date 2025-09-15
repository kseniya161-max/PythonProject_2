from abc import ABC, abstractmethod
from typing import Any, Dict
import os
import json


class FileHandler(ABC):
    """Абстрактный класс для работы с файлами."""

    @abstractmethod
    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        """Добавляет вакансию в файл."""
        pass

    @abstractmethod
    def _load_vacancies(self):
        """Загружаем вакансию из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: int) -> None:
        """Удаляет вакансию из файла по ID."""
        pass

    @abstractmethod
    def _save_vacancies(self) -> None:
        """Созраняет"""
        pass


class Saving(FileHandler):
    """Класс который реализует методы для работы с json файлом"""
    def __init__(self, filename = "vacancies.json"):
        self._filename = filename
        self.vacancies = self._load_vacancies()

    def _load_vacancies(self):
        """Выгрузка вакансий из json файла"""
        if os.path.exists(self._filename):
            with open(self._filename, "r", encoding = "UTF-8") as f:
                return json.load(f)
        return []

    def add_vacancy(self, vacancy_data: Dict[str, Any]) -> None:
        """Добавление вакансий"""
        if not any(vacancy.get("id") == vacancy_data.get("id") for vacancy in self.vacancies):
            self.vacancies.append(vacancy_data)
            self._save_vacancies()
        else:
            print("Вакансия с таким ID уже существует.")

    def _save_vacancies(self) -> None:
        """Сохранение вакансий в JSON файл."""
        with open(self._filename, "w", encoding="UTF-8") as f:
            json.dump(self.vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy_id):
        """Удаление"""
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy.get("id") != vacancy_id]
        self._save_vacancies()


# if __name__ == "__main__":
#     # Создаем экземпляр Saving для другого файла
#     saving_handler = Saving(filename="my_vacancies.json")
#
#     # Добавляем вакансии
#     vacancy_data = {
#         "id": 1,
#         "name": "Программист Python",
#         "link": "https://example.com/vacancy/1",
#         "salary": 80000,
#         "description": "Ищем опытного программиста Python."
#     }
#     saving_handler.add_vacancy(vacancy_data)
#
#     # Удаление вакансии
#     saving_handler.delete_vacancy(vacancy_id=1)
#
#     # Текущие вакансии
#     print(saving_handler.vacancies)
#
#     # Создаем еще один
#     other_saving_handler = Saving(filename="other_vacancies.json")
#
#    #Добавления вакансии в другой файл
#     other_vacancy_data = {
#         "id": 2,
#         "name": "Программист Java",
#         "link": "https://example.com/vacancy/2",
#         "salary": 90000,
#         "description": "Ищем опытного программиста Java."
#     }
#     other_saving_handler.add_vacancy(other_vacancy_data)
#
#     # Текущие вакансии
#     print(other_saving_handler.vacancies)


