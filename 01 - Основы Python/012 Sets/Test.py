rainbow_colors = {'red', 'orange', 'yellow',
                  'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 442, 524]
text_tuple = ('number', 'text', 'index')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')

print(set_from_list)
print(set_from_tuple)
