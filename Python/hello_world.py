command = ''
while True :
    command = input(">").lower()
    if command == 'help' :
        print("""
start - starts the car
stop - stops the car
quit - quits the game
        """)
    elif command == 'start':
        print("Car started...Ready to go"
    elif command == 'stop' :
        print("Car stopped.")
    elif command == 'quit' :
        print('game quitted')
        break
    else :
        print("Sorry I don't understand")
