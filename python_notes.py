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

#####

