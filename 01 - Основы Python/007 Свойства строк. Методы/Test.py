# Immutable
firstName = 'Jake'
print(firstName[2])

# firstName[2] = 'n'
# print(firstName)

firstToLetters = firstName[:2]
print(firstToLetters)

LastLetters = firstName[-1:]
print(LastLetters)

# Concatenable

newFirstName = firstToLetters + 'n' + LastLetters

print(newFirstName)
