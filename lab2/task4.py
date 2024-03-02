import random


def guess_number():
    number_to_guess = random.randint(1, 9)
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        user_input = int(input("Введите число от 1 до 9: "))
        if user_input < number_to_guess:
            print("Ваше число меньше.")
        elif user_input > number_to_guess:
            print("Ваше число больше.")
        else:
            print("Вы угадали!")
            return
        attempts += 1

    print(f"Попытки закончились. Загаданное число было: {number_to_guess}")


if __name__ == '__main__':
    while True:
        guess_number()
        play_again = input("Хотите сыграть еще раз? (Да/Нет): ")
        if play_again.lower() == "нет":
            exit(1)
