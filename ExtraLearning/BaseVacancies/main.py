from CompaniesInformation import CompaniesInformation
from Company import Company
from Vacancy import Vacancy

if __name__ == "__main__":

    # Добавить информацию об организациях
    c = CompaniesInformation()
    c.addCompany(Company("Sber", "Moscow", "5555"))
    c.addCompany(Company("Wildberries", "Moscow", "2222"))
    c.addCompany(Company("Sber2", "Moscow", "5555"))

    # Удалить информацию об организациях
    c.removeCompany("Sber2")

    c.addCompany(Company("Yandex", "Moscow", "1111"))

    # Добавить информацию в вакансиях в организации
    c.addVacancy(Vacancy("Yandex", "SMM", "Content manager", "...", 2000))
    c.addVacancy(Vacancy("Yandex", "SMM", "Reels maker", "...", 2500))
    c.addVacancy(Vacancy("Yandex", "SMM", "Stories maker", "...", 3500))
    c.addVacancy(Vacancy("Yandex", "Development", "Junior Python Developer", "...", 1000))
    c.addVacancy(Vacancy("Yandex", "Development", "Middle Python Developer", "...", 2500))
    c.addVacancy(Vacancy("Yandex", "Development", "Senior Python Developer", "...", 4500))
    c.addVacancy(Vacancy("Yandex", "Analyst", "System analyst", "...", 2700))
    c.addVacancy(Vacancy("Yandex", "Analyst", "Product analyst", "...", 4000))
    c.addVacancy(Vacancy("Yandex", "Analyst", "Business analyst", "...", 6500))

    c.addVacancy(Vacancy("Sber", "Development", "Middle C# Developer", "...", 5500))
    c.addVacancy(Vacancy("Sber", "Development", "Middle Java Developer", "...", 4500))

    c.addVacancy(Vacancy("Wildberries", "Development", "Middle C++ Developer", "...", 5000))
    c.addVacancy(Vacancy("Wildberries", "Development", "Junior C++ Developer", "...", 5000))
    c.addVacancy(Vacancy("Wildberries", "Development", "Senior C++ Developer", "...", 5000))

    # Удалить информацию в вакансиях в организации
    c.removeVacancy("Sber", "Development", "Middle C# Developer")
    c.removeVacancy("Yandex", "SMM", "Content manager")

    # Просмотреть полною информацию о вакансиях
    c.printAllVacancies()

    # Просмотреть информацию о вакансиях в конкретной организации
    c.printVacanciesByCompany("Yandex")
    c.printVacanciesByCompany("Sber")

    #Поиск вакансий по специальности
    c.searchVacancyBySpecialization("Development")

