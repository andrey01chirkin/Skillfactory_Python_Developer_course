from datetime import date
from typing import List, Dict, Any


def calculate_age(birth_date: str) -> int:
    birth_year, birth_month, birth_day = [int(item) for item in birth_date.split('-')]
    today = date.today()
    return today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))


def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return list(filter(lambda item: calculate_age(item['birth_date']) > 18, users))


def generate_username(first_name: str, last_name: str) -> str:
    return f"{first_name[0].lower()}.{last_name.lower()}"


print(calculate_age("1990-05-15"))
# 34
users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]

print(filter_adults(users_data))
# [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'}]
print(generate_username("John", "Doe"))
# "j.doe"

