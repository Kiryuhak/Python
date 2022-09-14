car_price = {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
print(car_price)
print(car_price['opel'])

# Добовляем новый объект
car_price['mazda'] = 4000
print(car_price)

# Удалить объект
del car_price['toyota']
print(car_price)
# чистка
car_price.clear()
print(car_price)

person = {
    'firstName': 'John',
    'lastName': 'Smith',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daugter': 'Pamela'}
}

print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])

print(person['hobbies'][1])

print(person['children']['son'])
person['car'] = 'Mazda'
person['hobbies'][0] = 'basketball'
print(person)

print(person.keys())
print(person.values())
