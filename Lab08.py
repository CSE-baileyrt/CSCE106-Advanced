# The purpose of this lab is to demonstrate mastery of Python classes and code comprehension

### PART 1 ###
# Complete the "to-do" items below
# TODO: 1.1 Create a Person class in Python that satisfies the instance below
# hint: no class functions needed, just properties (members)

# Instance: first name, last name, job title, email address, state
mr_Bailey = Person("Robert", "Bailey", "Instructor", "baileyrt@cse.sc.edu", "SC")


# TODO: 1.2 use clues in the Pet class to fill in the missing pieces
class Pet:
    # function missing here

    def feed(self):
        print('It is time for {} to eat {}'.format(self.name, self.food))

    def greet(self):
        print('Hello, my name is {}, I am a {}, and my owner is {}'.format(self.name, self.type, self.owner))

rover = Pet("Rover", "dog", "kibble", "Mary")
princess = Pet("Princess", "cat", "tuna", "Mary")
rover.greet()
princess.greet()
rover.feed()
princess.feed()


# TODO: 1.3 create a UsedCar class
# details: year, make, model, mileage, price

# TODO: 1.4 create 3 instances of UsedCar
# 1. your car (or a friend's car, or just make one up)
# 2. 2027 Volkswagen ID.Buzz, brand new, for $60,000
# 3. a car you imagine Tom Holland would drive

# TODO: 1.5 create a custom class
# you decide the details; at least 3 properties and 1 function

# TODO: 1.6 create 2 instances of your custom class
# you may create more than 2, if you wish


### PART 2 ###
# NOTE: Exercise 2.2 below asks you to make a GUESS.
#       You will NOT lose any points if you guess wrong.
#       The point is to think, analyze, and make an educated guess.

# TODO: 2.1 review the following code (just look at it, think about it)
print('twos\tthrees\tfours\tfives\tsixes\tsevens\teights\tnines\ttens')
for i in range(2, 11):
    one_line = ''
    for j in range(2, 11):
        mult = '{}x{}={}\t'.format(j, i, i*j)
        one_line += mult
    print(one_line)

# TODO: 2.2 do NOT execute the code, but do write what you think is does
# right here, in a comment:

# TODO: 2.3 execute the code, then write what it actually did
# right here, in a comment:

# TODO: 2.4 if you have any questions about the code (part 2), write them
# right here, in a comment:
