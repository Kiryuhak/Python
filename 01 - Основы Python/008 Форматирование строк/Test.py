name = 'John'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old'.format(name, age)
print(name_and_age)

name_and_age = 'My name is {0}. I\'m {1} years old'.format('Jack', 23)
print(name_and_age)

week_days = 'There are 7 days of week: {su}, {mo}, {tu}, {we}, {th}, {fr}, {sa}'.format(
    mo="Monday", we="Wednesday", tu="Thursday", fr="Friday", sa="Saturday", su='Sunday')
print(week_days)
