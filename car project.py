command=""
started=False
stopped=False
while command != 'quit':
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("car is already starte")
        else:
            started=True
            print("Car started,ready 'to go")
    elif command == 'stop':
        if stopped:
            print("Already stop")
        else:
            stopped=True
            print("car stopped")
    elif command == 'help':
        print('''
 start --> To start the car
 stop --> To stop the car
 quit --> To exit''')
    elif command == 'quit':
        print('Terminated')

    else:
         print(" I don't understand")






