# Started Feb 23: Notes from https://www.youtube.com/watch?v=_uQrJ0TkZlc

##### if/elif/else

is_hot = False
is_cold = False

if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")

# Would print “Its a lovely day” “Enjoy your day” 

##### f string

first = "John"
last = "[Smith]"
print(f'{first} {last} is a coder')

# Would print “John [Smith] is a coder”

##### if/else and f string

good_credit = True
bad_credit = False

home_price = 1000000

if good_credit:
    down_payment = (int(home_price * .1))
else:
    down_payement = (int(home_price * .2))

print(f'Your Down Payment is ${down_payment}')

# Would return “Your Down Payment is $100000”

##### if/and/or/not

name_over_3 = False
name_under_50 = False
good_name = "Heck yeah brother"
bad_name = "Sorry friend."
too_short = "Your name has to be over 3 characters."
too_long = "Your name has to be under 50 characters."
short_and_long = "Somehow you made this both too short and too long"
proceed_instruction = "Proceed with excellence."


if not name_over_3 or not name_under_50:
    print(bad_name)
else:
    print(good_name)

if name_over_3 and not name_under_50:
    print(too_long)
elif name_under_50 and not name_over_3:
    print(too_short)
elif name_under_50 and name_over_3:
    print(proceed_instruction)
else:
    print(short_and_long)

# would print “Somehow you made this both too short and too long”

##### based on length

name = "Nathan"
too_short = "Needs to be at least three characters"
too_long = "Needs to be less than 10 characters"
good_name = "Heck yeah brother"

if len(name) < 3:
    print(too_short)
elif len(name) > 10:
    print(too_long)
else:
    print(good_name)

# would print Heck yeah brother

##### Weight converter

weight = int(input('Weight: '))
unit = input('Pounds or Kilos: ')

if unit.upper() == "POUNDS":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == "KILOS":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("Please select either Pounds or Kilos.")

##### While loops

i = 1
while i <= 5:
    print(i)
    i = i + 1

print("Done")

# prints:

 # 1
 # 2
 # 3
 # 4
 # 5
 # Done

##### Guessing game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

##### car game

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        print("Game over.")
        break
    else:
        print("Sorry, I don't understand that. Type 'help' for help.")


##### For loop

prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"Total: {total}")

# this adds all the prices together

##### Nested loops

numbers = [1, 1, 1, 1, 9]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# prints an L shape of x's

##### largest number find using for loop and lists

moral_scores = [3, 6, 2, 8, 4, 10]
most_moral = moral_scores[0]

for how_moral in moral_scores:
    if how_moral > most_moral:
        most_moral = how_moral
print(how_moral)

# this would print 10 because 10 is the highest moral_score

##### 2d lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)


##### search in index

words = ["pizza", "chips", "cookies", "bread", "beer"]
print(("pizza" or "poison") in words)
# would return true because pizza is in there

##### append and copy in list

numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)

# prints
# [5, 2, 1, 5, 7, 4, 10]
# [5, 2, 1, 5, 7, 4]

##### remove duplicates in a list

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

###### unpacking

coordinates = [1, 2, 3]

x, y, z = coordinates
# ^that^ does the same as below
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

##### dictionary

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])
print(customer["name"])
# prints Jan 1 1980
# prints John Smith

##### Moral game v1

command = ""
immoral_values = ["stealing", "stole", "lying", "lied", "hurt", "cheat"]
moral_values = ["help", "give", "love", "charity", "build"]
input_prompt = input("What happened?: ")
word_list = input_prompt.split()
moral_weight = 0

for word in word_list:
    if word.lower() in immoral_values:
        moral_weight += -1
    elif word.lower() in moral_values:
        moral_weight += 1
    else:
        moral_weight += 0
print(f"Moral Score: {moral_weight}")

# "I love you" would have a moral score of 1, "I hate you" would be -1, and "I hate and love you" as 0"

### dictionary split for and get method

message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "☹️"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
# entering "hello :( :)" would print hello (frown emoji) (happy emoji)

####
















