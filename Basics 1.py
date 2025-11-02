print("hey")


for i in range(5):
    print("Doing important work. i =", i)


i = 0 
while i < 10:
    print("lets count to ", i)
    i = i + 1

squeares = [n**2 for n in range(10)]
squeares

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

shortplanets = [planet for planet in planets if len(planet) < 6]
shortplanets



loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

my_list = [1, -10, 5, -3, 0]


claim = "Pluto is a planet!"

spliting = claim.split()
spliting


datess = "1991-01-01"
splitted = datess.split('-')
splitted



pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

"{} weighs {:.1}kgs and  ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass / earth_mass, population,)


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)

numbers = {'One':1, 'Two': 2, 'Three': 3}
numbers['One']


for k in numbers: 
    print('{} = {}'.format(k, numbers[k]))


import math

print("It's math! It has type {}".format(type(math)))

print(dir(math))


print("pi to the 4th digit = {:.4}".format(math.pi))

#visszafele leirja szot 

szo = "alma"


def reverse_string(text):
    reversed_word = ""
    # I chose the name 'letter' this time
    for letter in text:
        reversed_word = letter + reversed_word
    return reversed_word

print(reverse_string("kaki"))

print ("hey")

def reverse_string(text):
    reversed_word = ""
    # I chose the name 'letter' this time
    for letter in text:
        reversed_word = letter + reversed_word
    return reversed_word

print(reverse_string("Jhon"))



def reverse_string(text):
    reversed_word = ""
    # I chose the name 'letter' this time
    for letter in text:
        reversed_word = letter + reversed_word
    return reversed_word

print(reverse_string("Jhonny"))



