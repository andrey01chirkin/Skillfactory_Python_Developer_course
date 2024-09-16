from typing import List, Dict, Any


# А также вам наверняка может понадобиться модуль functools...

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    return [f"{item['first_name']} {item['last_name']}" for item in users]


def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    #return {user['email'] for user in users1 if user['email'] == user['email'] for user in users2}
    emails = set()
    for user in users_data_ext:
        for user_ in users_data:
            if user['email'] == user_['email']:
                emails.add( user['email'])
    return emails

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    result = {}
    for user in users:
         print(user.items())


users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'}]

users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}]

print(convert_to_full_name(users_data))
# ['John Doe', 'Bob Johnson', 'Lev Sergeev']
print(find_matching_emails(users_data, users_data_ext))
# {'johndoe@gmail.com'}
print(combine_user_data(users_data))
# {'first_name': ('John', 'Bob', 'Lev'), 'last_name': ('Doe', 'Johnson', 'Sergeev'), 'birth_date': ('1990-05-15', '1985-10-22', '2015-01-01'), 'email': ('johndoe@gmail.com', 'bobJ@gmail.com', 'lev46@gmail.com')}
