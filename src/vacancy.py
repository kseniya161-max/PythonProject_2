from src. options import Connect
import json

class VacancyWorking():
    __slots__ = ('name', 'link', 'salary', 'description')

    def __init__(self, name: str, link: str, salary: int, description: str):
        self.name = name
        self.link = link
        self.salary = self._validate_salary(salary)
        self.description = description

    def _validate_salary(self,salary: int):
        """Приватный метод для валидации зарплаты"""
        if salary is None:
            return 0
        elif salary < 0:
            raise ValueError("Заработная плата не может быть ниже 0")
        return salary

    def salary_compare(self):
        """Метод об отображении заработной платы"""
        if self.salary <= 0:
            return "Заработная плата ровна 0"
        else:
            return f"Заработная плата по  позиции {self.name} составляет: {self.salary}"

    def to_dict(self):
        """Метод для преобразования объекта в словарь"""
        return {
            "name": self.name,
            "link": self.link,
            "salary": self.salary,
            "description": self.description
        }

    def __lt__(self, other):
        """Магический метод который сравнивает зарплату "Меньше"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод который сравнивает зарплату "Больше"""
        return self.salary > other.salary


if __name__ == "__main__":
    api = Connect()
    vacancies_data = api.vacancies("разработчик")

    vacancies = []
    if vacancies_data:
        for data in vacancies_data:
            if data is not None:
                name = data.get('name', 'Нет названия')
                link = data.get('alternate_url', 'Нет ссылки')
                salary_info = data.get('salary')
                salary = salary_info['from'] if salary_info and 'from' in salary_info else 0
                description = data.get('snippet', {}).get('requirement', 'Нет описания')
                vacancies.append(VacancyWorking(name, link, salary, description))
            else:
                print("Получены пустые данные для вакансии.")  # Выводим сообщение, если data None
    else:
        print("Нет данных о вакансиях.")
    vacancies_list = [vacancy.to_dict() for vacancy in vacancies]
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies_list, f, ensure_ascii=False, indent=4)

    print("Данные о вакансиях успешно сохранены в файл vacancies.json.")
