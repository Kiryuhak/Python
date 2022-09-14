tuple_1 = (1, 2, 3)
tuple_2 = ('one', 'hi', 'three')
tuple_3 = (3, 2.3, 'three')

# tuple_1[1] = 3

new_tuple = (tuple_1[0], 5, tuple_1[2])
print(new_tuple)

print(tuple_1)
print(tuple_2)
print(tuple_3)

x = y = z = 12
print(x, y, z)

x, y, z = 12, 13, 14

print(x, y, z)

person_tuple = ('John', 'Smith', 1995)
firstName, lastName, year_of_birth = person_tuple

print(firstName, lastName, year_of_birth)

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(1))

greeting_tuple = ('John', 'hello', 'hi', 'John')
print(greeting_tuple.count('John'))

print(t1.index(5))
print(greeting_tuple.index('hello'))
