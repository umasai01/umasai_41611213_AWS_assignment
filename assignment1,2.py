import random   #Cows and Bull using conditional & looping statements


def compare_numbers(secret_number, user_guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            cows += 1
        elif user_guess[i] in secret_number:
            bulls += 1
    return cows, bulls

def main():
    secret_number = str(random.randint(1000, 1004))
    num_guesses = 0

    print(" Cows and Bulls Game!")

    while True:
        user_guess = input("Enter a 4-digit number: ")

        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        num_guesses += 1
        cows, bulls = compare_numbers(secret_number, user_guess)

        if user_guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} in {num_guesses} guesses.")
            break
        else:
            print(f"{cows} cows, {bulls} bulls")

if __name__ == "__main__":
    main()