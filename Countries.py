# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
#
# city = input()
#
# for i, j in countries.items():
#     # print(i)
#     if city in j:
#         print(f'INFO: {city} is a city in {i}')
#         break
# else:
#     print(f'ERROR: Country for {city} not found')

user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}
# for i in user.items():
#     if 'password' in i:
#         x = i[1]
#     elif 'last_name' in  i:
#         y = i[1]
# user.pop('password')
# user.pop('last_name')
#
# user.setdefault('secret', x)
# user.setdefault('surname', y)
user['secret'] = user.pop('password')
user['surname'] = user.pop('last_name')
print(user)