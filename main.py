# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.


students = ['Laura', 'John', 'Chris', 'Min', 'Sri']

# print(students[1])
# print(students[-1])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "{food goes here} is a good food"

foods = ('salad', 'pizza', 'hamburger', 'cake', 'pie')

# for food in foods:
#     print(f'{food} is a good food')


# Exercise 3
# Using a for loop, print just the last two food strings from foods.

# for i in range(len(foods) - 2, len(foods)):
#     print(foods[i])

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    'city': 'Seattle',
    'state': 'Washington',
    'population': 744955,
}

# print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"


# for key in home_town.keys():
#     print(f'{key} = {home_town[key]}')

# Exercise 6
# Create an empty list named cohort.

# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#  {
#  	'student': 'Tina',
#  	'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.

cohort = []

# for i in range(0, len(students)):
#     cohort.append({'student': students[i], 'fav_food': foods[i]})

# for i in range(0, len(cohort)):
#     print(cohort[i])

# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

awesome_students = [f'{student} is awesome' for student in students]

# for i in range(0, len(awesome_students)):
#     print(awesome_students[i])

# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.

# print([food for food in foods if 'a' in food])