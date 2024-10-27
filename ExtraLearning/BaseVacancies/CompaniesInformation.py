from Company import Company
from Vacancy import Vacancy
from pprint import pformat
from accessify import private

class CompaniesInformation:
    def __init__(self):
        self.__companies_information = {}
        self.__companies_vacancies = {}

    @private
    def __printCompaniesInformation(self):
        print("Информация о компаниях:")
        print(pformat(self.__companies_information, indent=2, depth=4))

    def addCompany(self, company: Company):
        if not self.__companies_information.get(company.name):
            self.__companies_information[company.name] = {
                "location": company.location,
                "phone": company.phone
            }
            print(f"\nКомпания {company.name} добавлена")
            self.__printCompaniesInformation()
        else:
            print("\nТакая компания уже существует")
            self.__printCompaniesInformation()

    def removeCompany(self, name_company):
        if self.__companies_information.get(name_company):
            del self.__companies_information[name_company]
            print(f"\nКомпания {name_company} удалена")
            self.__printCompaniesInformation()
        else:
            print("\nТакой компании не существует")
            self.__printCompaniesInformation()

    @private
    def __getDataVacancy(self, description, salary):
        return {
            "description": description,
            "salary": salary
        }

    def printAllVacancies(self):
        print("Вакансии компаний:")
        print(pformat(self.__companies_vacancies, indent=1, width=100, depth=4))

    def printVacanciesByCompany(self, company):
        if not self.__companies_vacancies.get(company):
            print(f"Компания \"{company}\" не существует")
            return
        print(f"Вакансии компании \"{company}\":")
        print(pformat(self.__companies_vacancies[company], indent=1, width=100, depth=4))

    def addVacancy(self, vacancy: Vacancy):
        if not self.__companies_information.get(vacancy.company):
            print(f"Компания \"{vacancy.company}\" не существует !!!")
            return

        if not self.__companies_vacancies.get(vacancy.company):
            self.__companies_vacancies[vacancy.company] = {
                vacancy.specialization: {
                    vacancy.name: self.__getDataVacancy(vacancy.description, vacancy.salary)
                }
            }
            print(f"\nВакансия \"{vacancy.name}\" добавлена в компанию \"{vacancy.company}\" по специальности \"{vacancy.specialization}\"")
            self.printAllVacancies()

        if not self.__companies_vacancies[vacancy.company].get(vacancy.specialization):
            self.__companies_vacancies[vacancy.company][vacancy.specialization] = {
                vacancy.name: self.__getDataVacancy(vacancy.description, vacancy.salary)
            }
            print(f"\nВакансия \"{vacancy.name}\" добавлена в компанию \"{vacancy.company}\" по специальности \"{vacancy.specialization}\"")
            self.printAllVacancies()

        self.__companies_vacancies[vacancy.company][vacancy.specialization][vacancy.name] = self.__getDataVacancy(vacancy.description, vacancy.salary)
        print(f"\nВакансия \"{vacancy.name}\" добавлена в компанию \"{vacancy.company}\" по специальности \"{vacancy.specialization}\"")
        self.printAllVacancies()

    def removeVacancy(self, company, specialization, name_vacancy):
        if not self.__companies_vacancies.get(company):
            print(f"Компания \"{company}\" отсутствует")
            return

        if not self.__companies_vacancies[company].get(specialization):
            print(f"Специальность \"{specialization}\" отсутствует в компании {company}")
            return

        if not self.__companies_vacancies[company][specialization].get(name_vacancy):
            print(f"Вакансия \"{name_vacancy}\" отсутствует в компании \"{company}\"")
            return

        del self.__companies_vacancies[company][specialization][name_vacancy]
        print(f"Вакансия \"{name_vacancy}\" по специальности \"{specialization}\" удалена из компании \"{company}\"")
        self.printAllVacancies()

    def searchVacancyBySpecialization(self, specialization):
        there_is_specialization = False
        for name_company, vacancy in self.__companies_vacancies.items():
            if vacancy.get(specialization):
                print(f"\nВакансии  компании \"{name_company}\" по специальности \"{specialization}\":")
                print(pformat(vacancy[specialization], indent=1, width=100, depth=4))
                there_is_specialization = True

        if not there_is_specialization:
            print(f"\nСпециализация \"{specialization}\" отсутствует")