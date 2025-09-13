from src. options import Connect

if __name__ =="__main__":
    api = Connect()
    api.connection()
    vacancies = api.vacancies()
    for vacancy in vacancies:
        print(vacancy['name'], vacancy['url'])