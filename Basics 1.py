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




print('hey')



def reverse_string(text):
    reversed_word = ""
    # I chose the name 'letter' this time
    for letter in text:
        reversed_word = letter + reversed_word
    return reversed_word

print(reverse_string("xcssds"))



def reverse_string(text):
    reversed_word = ""
    # I chose the name 'letter' this time
    for letter in text:
        reversed_word = letter + reversed_word
    return reversed_word

print(reverse_string("dffsdf"))



number = [i for i in range(11)]
print(number)

squared = [i*i for i in range(11)]
print(squared)

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negatives = [i for i in numbers if i < 0]
print(negatives)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

newlist = [list for list1 in list_of_lists for list2 in list1 for list in list2]
print(newlist)


weird = [(i, 1, i, i**3, i**4, i**5) for i in range(11)]

for item in weird:
    print(weird)

# The loop variable 'i' goes from 0 to 10.
# The tuple elements are i, 1, and then i to the power of 1, 2, 3, 4, and 5.
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# Print the result
for item in result:
    print(item)


def absolute (x):
    if x >= 0:
        return x
    else:
        return -(x)

print(absolute(-1))

def add_ten():
    ten = 10

    def add(num):
        return num + 10
    return add

closure_result = add_ten()
print(closure_result(10))


multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
