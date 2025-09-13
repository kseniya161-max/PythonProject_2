from abc import ABC, abstractmethod
import requests
import json


class BaseClass(ABC):
    @abstractmethod
    def connection(self):
        pass

    @abstractmethod
    def vacancies(self):
        pass

class Connect(BaseClass):
    """Класс подключения к API"""
    base_url = "https://api.hh.ru/"

    def __init__(self):
        self.session = None

    def connection(self):
        """Подключение к API"""
        self.session = requests.Session()
        print ("Успешное подключение к API")

    def vacancies(self):
        """ Получение вакансий"""

        if self.session is None:
            print("Сначала необходимо установить соединение.")
            return []
        response = self.session.get(self.base_url + "vacancies")
        if response.status_code == 200:
            vacancies = response.json().get("items", [])
            return vacancies
        else:
            print(f"Нет подключения: {response.status_code}")
            return []




