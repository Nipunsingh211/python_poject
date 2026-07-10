import random

print("===Guess the no between 1 to 100===")

def pc(ch):
    if ch == 1:
        return random.randint(1, 5)
    elif ch == 2:
        return random.randint(1, 50)
    elif ch == 3:
        return random.randint(1, 100)
    else:
        return None

while True:
    print("\n1. Easy   : 1-5")
    print("2. Medium : 1-50")
    print("3. Hard   : 1-100")
    ch = int(input("Enter your choice: "))

    pc_no = pc(ch)
    if pc_no is None:
        print("Invalid choice, try again.")
        continue

    attempts = 0
    max_attempts = 10

    while True:
        no_of_time_user_guess = int(input("Enter the no: "))
        attempts += 1

        if pc_no == no_of_time_user_guess:
            print("Congratulations! Right guess, the no is:", pc_no)
            break
        elif pc_no < no_of_time_user_guess:
            print("THE NO IS TOO HIGH")
        else:
            print("THE NO IS TOO LOW")

        print("Attempts made:", attempts)

        if attempts == max_attempts:
            print("Sorry! You lost the game. The number was:", pc_no)
            break

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break