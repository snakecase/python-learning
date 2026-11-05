print('Rock and Stone!!')
print("What's your age?") # Ask for their age

while True:
    try:
        my_age = int(input('>'))

        # Validate the age
        if 0 < my_age <= 120:
            break
        else:
            print('Please enter a realistic age between 1 and 120')

    except ValueError:
        print('Invalid input. Please enter a number.')

print("I'm " + str(my_age) + ' years old')
print('The sum of your age digits is: ' + str(sum(int(digit) for digit in str(my_age))))
print("You'll be " + str(my_age + 2) + ' years old two years later.')