import random
print("Welcome to the 21 game ")

print("Do you want to go first or second? ")

choice = input().lower()

if choice == "first":
    print(f"You start first\n")
if choice == "second":
    print(f"You start second\n")
list_of_numbers = []
def player_turn(list_of_numbers):
    number = int(input("How many numbers do you wish to enter "))
    for i in range(len(list_of_numbers),len(list_of_numbers)+number+1):
        list_of_numbers.append(i)
    return list_of_numbers

def computer_turn(current):
    numbers = []
    for _ in range(1):
        if current < 21:
            number = random.randrange(1,4)
            if current + number > 21:
                break
            else:
                current += number
        else:
            break
        numbers.append(number)
    return numbers , current

def gameOfTwentyOne():
    total = 0 
    while total < 21:
        print(f"Current total is: {total}")
        if choice == "first":
            player_input = int(input("Enter number between 1 and 3 "))
            try:
                if player_input < 1 or player_input > 3:
                    print("Invalid number, please enter a number between 1 and 3 ")
                    continue
            except ValueError:
                print("Invalid number, please enter a number between 1 and 3 ")
                continue
            total += player_input

            if total >= 21:
                print(f"Current total is {total}")
                print("Player loses! The total reached or exceeded 21. ")
                return
            numbers , total = computer_turn(total)

            print(f"Computer generated numbers: {numbers}")
            print(f"New Total: {total}")
            if total >= 21:
                print("Computer loses! The total reached or exceeded 21.")
                return
        else:
            numbers , total = computer_turn(total)

            print(f"Computer generated numbers: {numbers}")
            print(f"New Total: {total}")
            if total >= 21:
                print("Computer loses! The total reached or exceeded 21.")
                return
            player_input = int(input("Enter number between 1 and 3 "))
            try:
                if player_input < 1 or player_input > 3:
                    print("Invalid number, please enter a number between 1 and 3 ")
                    continue
            except ValueError:
                print("Invalid number, please enter a number between 1 and 3 ")
                continue
            total += player_input

            if total >= 21:
                print(f"Current total is {total}")
                print("Player loses! The total reached or exceeded 21. ")
                return
           
gameOfTwentyOne()
        