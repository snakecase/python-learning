print('Rock and Stone!!')
print("What's your age?") # Ask for their age

while True:
    my_age = input('>')
    try:
        my_age_int = int(my_age)

        # Validate the age
        if 0 < my_age_int <= 120:
            break
        else:
            print('Please enter a realistic age between 1 and 120')

    except ValueError:
        print('Invalid input. Please enter a number.')

print("I'm " + my_age + ' years old')
print('The sum of your age digits is: ' + str(sum(int(_) for _ in str(my_age) if _.isdigit())))
print("You'll be " + str(int(my_age) + 2) + ' years old two years later.')