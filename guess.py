import random as ran
# 1). Generate random number
# 2). Ask user for their number
# 3). Tell user result
# 4). Go back to step 2

# Generate random number
# <--- Number generation code
playing = True
while playing:
    
    saved_number = (ran.randint(1,100))
    print(saved_number)
    running = True
    life = 3

    while running:
        value = input('Guess the Number: ')
        print(value)
        if int (value)<saved_number:
            print('you wrote '+ value + ' which was too low')
            life = life - 1
        if int (value)>saved_number:
            print('you wrote '+ value + ' which is too high')
            life = life - 1
        if int (value)==saved_number:
            print('you wrote '+ value + ' which is correct!')
            running = False
        if life == 0:
            running = False

    again = input('Do it for the bois [yes/no]? ')
    if again != 'yes' and again != 'y' and again != 'yep' and again:
        playing = False
