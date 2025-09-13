from abc import ABC, abstractmethod
import requests
import json


class BaseClass(ABC):
    @abstractmethod
    def _connection(self):
        pass

    @abstractmethod
    def vacancies(self, keyword, per_page=20):
        pass


class Connect(BaseClass):
    """Класс подключения к API"""

    def __init__(self):
        self._session = None
        self._base_url = "https://api.hh.ru/"

    def _connection(self):
        """Подключение к API"""
        self._session = requests.Session()
        response = self._session.get(self._base_url)
        if response.status_code == 200:
            print("Успешное подключение к API")
        else:
            print(f"Ошибка подключения: {response.status_code}")

    def vacancies(self, keyword, per_page=20):
        """ Получение вакансий"""

        if self._session is None:
            self._connection()

        params = {"text": keyword, "per_page": per_page}
        response = self._session.get(self._base_url + "vacancies", params=params)
        if response.status_code == 200:
            vacancies = response.json().get("items", [])
            return vacancies
        else:
            print(f"Нет подключения: {response.status_code}")
            return []
