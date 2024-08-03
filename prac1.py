sqaure = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    player = 1
    status = -1
    while status == -1:
        board()
        if player % 2 == 1:
            player = 1
        else:
            player = 2

        print('\nPlayer', player)
        choice = int(input("Enter a number : "))

        if player == 1:
            mark = 'X'
        else:
            mark = 'O'

        if choice == 1 and sqaure[1] == 1:
            sqaure[1] = mark
        elif choice == 2 and sqaure[2] == 2:
            sqaure[2] = mark
        elif choice == 3 and sqaure[3] == 3:
            sqaure[3] = mark
        elif choice == 4 and sqaure[4] == 4:
            sqaure[4] = mark
        elif choice == 5 and sqaure[5] == 5:
            sqaure[5] = mark
        elif choice == 6 and sqaure[6] == 6:
            sqaure[6] = mark
        elif choice == 7 and sqaure[7] == 7:
            sqaure[7] = mark
        elif choice == 8 and sqaure[8] == 8:
            sqaure[8] = mark
        elif choice == 9 and sqaure[9] == 9:
            sqaure[9] = mark

        else:
            print("Invalid move")
            player -= 1

        status = game_status()
        player += 1

    print("RESULT")
    if status == 1:
        print("Player", player-1, 'win')
    else:
        print("Game Draw")


def game_status():
    if sqaure[1] == sqaure[2] and square[2] == square[3]:
        return 1
    elif sqaure[4] == sqaure[5] and square[5] == square[6]:
        return 1
    elif sqaure[7] == sqaure[8] and square[8] == square[9]:
        return 1
    elif sqaure[1] == sqaure[4] and square[4] == square[7]:
        return 1
    elif sqaure[2] == sqaure[5] and square[5] == square[8]:
        return 1
    elif sqaure[3] == sqaure[6] and square[6] == square[9]:
        return 1
    elif sqaure[1] == sqaure[5] and sqaure[5] == sqaure[9]:
        return 1
    elif sqaure[3] == sqaure[5] and sqaure[5] == sqaure[7]:
        return 1
    elif sqaure[1] != 1 and sqaure[2] != 2 and sqaure[3] != 3 and sqaure[4] != 4 and sqaure[4] != 4 and sqaure[5] != 5 and sqaure[6] != 6 and sqaure[7] != 7 and sqaure[8] != 8 and sqaure[9] != 9:
        return 0
    else:
        return -1


def board():
    print("\n\n\t TIC TAC TOE\n\n")

    print("Player 1(X) - Player 2(O)")
    print()

    print('     |     |     ')
    print(' ', sqaure[1], ' | ', sqaure[2], ' | ', sqaure[3])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', sqaure[4], ' | ', sqaure[5], ' | ', sqaure[6])

    print('_____|_____|_____')
    print('     |     |     ')

    print(' ', sqaure[7], ' | ', sqaure[8], ' | ', sqaure[9])
    print('     |     |     ')


main()
