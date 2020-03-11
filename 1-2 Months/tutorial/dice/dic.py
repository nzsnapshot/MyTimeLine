from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides


    def roll_die(self):
        return randint(1, self.sides)


# Builds a 6 sided dice and prints 10 results
d6 = Die()

results = []
for roll_number in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 Rolls of a 6 sided dice")
print(results)
# for result in results:
#     print(result)


print('\n')

# Builds a 10 sided dice and prints 10 results
d10 = Die(sides=10)

results = []

for roll_number in range(10):
    result = d10.roll_die()
    results.append(result)
print('10 rolls of a 10 sided dice')
print(results)

# for result in results:
#     print(result)

print('\n')
# Builds a 20 sided dice and prints 20 results
d20 = Die(sides=20)

results = []

for roll_number in range(20):
    result = d20.roll_die()
    results.append(result)
print('20 Rolls of a 20 sided dice')
print(results)

# for result in results:
#     print(result)
