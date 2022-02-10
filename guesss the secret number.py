secret_number=7
no_of_try=3
count_try=0
while count_try< no_of_try:
    guess=int(input('guess: '))
    count_try = count_try+1
    if guess == secret_number:
        print('you won')
        break
else:
    print("no more try")
