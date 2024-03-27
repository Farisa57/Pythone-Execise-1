def game():

    guess = int(input())

    num = 6

    if guess == num:
        print("Your answer is correct")

    elif guess<num:
        print("Your guess is almost there")

    elif guess>num:
        print("Your guess is higher")


game()


