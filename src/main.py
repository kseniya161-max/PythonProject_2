from src. options import Connect

if __name__ =="__main__":
    api = Connect()
    vacancies = api.vacancies("разработчик")
    for vacancy in vacancies:
        print(vacancy['name'], vacancy['url'])