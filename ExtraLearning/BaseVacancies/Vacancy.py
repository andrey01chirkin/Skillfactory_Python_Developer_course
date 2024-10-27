
class Vacancy:
    def __init__(self, company, specialization, name, description, salary):
        self.__company = company
        self.__specialization = specialization
        self.__name = name
        self.__description = description
        self.__salary = salary

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        self.__company = company

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        self.__specialization = specialization

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

