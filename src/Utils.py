from typing import List, Dict, Any


def print_vacancies(vacancies_data: List[Dict[str, Any]]) -> None:
    """Выводит список вакансий"""
    for i, data in enumerate(vacancies_data, start=1):
        name = data.get("name", "Нет названия")
        link = data.get("link", "Нет ссылки")
        salary_info = data.get('salary')
        salary = salary_info["from"] if salary_info and "from" in salary_info else 0
        print(f"{i}.{name} - {salary} - {link}")


def get_vacancies(api, keyword: str) -> List[Dict[str, Any]]:
    """Получает вакансии по ключевому слову."""
    return api.vacancies(keyword)


def filter_vacancies_by_keyword(vacancies_data: List[Dict[str, Any]], keyword: str) -> List[Dict[str, Any]]:
    """Фильтрует вакансии по ключевому слову в описании."""
    return [
                data for data in vacancies_data
                if data.get('snippet') and data['snippet'].get('requirement') and keyword.lower()
                   in data['snippet']['requirement'].lower()
            ]
