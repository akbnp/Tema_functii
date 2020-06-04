import random

board = [" " for i in range(10)]


def insert_Letter(letter, pos):
    board[pos] = letter

def space_Is_Free(pos):
    return board[pos] == " "

def print_Board(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])

def is_Winner(board, letter):
    return (
        (board[7] == letter and board[8] == letter and board[9] == letter)
        or (board[4] == letter and board[5] == letter and board[6] == letter)
        or (board[1] == letter and board[2] == letter and board[3] == letter)
        or (board[1] == letter and board[4] == letter and board[7] == letter)
        or (board[2] == letter and board[5] == letter and board[8] == letter)
        or (board[3] == letter and board[6] == letter and board[9] == letter)
        or (board[1] == letter and board[5] == letter and board[9] == letter)
        or (board[3] == letter and board[5] == letter and board[7] == letter)
    )


def player_Move():
    run = True
    while run:
        move = input("Alege o pozitie pentru 'X' (1-9): ")
        try:
            move = int(move)
            if 0 < move < 10:
                if space_Is_Free(move):
                    run = False
                    insert_Letter("X", move)
                else:
                    print("E deja ocupat!")
            else:
                print("Alege un numar intre 1 si 9!")
        except:
            print("Alege un numar!")


def comp_Move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let

            if is_Winner(boardCopy, let):
                move = i
                return move

    if 5 in possibleMoves:
        move = 5
        return move

    corner = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corner.append(i)

    if len(corner) > 0:
        move = select_Random(corner)
        return move

    lateral = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            lateral.append(i)

    if len(lateral) > 0:
        move = select_Random(lateral)

    return move


def select_Random(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def board_Full(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


def program():
    print("X si 0")
    print_Board(board)

    while not (board_Full(board)):
        if not (is_Winner(board, "O")):
            player_Move()
            print_Board(board)
        else:
            print("Ai pierdut!")
            break

        if not (is_Winner(board, "X")):
            move = comp_Move()
            if move == 0:
                print("Egalitate!")
            else:
                insert_Letter("O", move)
                print("Computerul a pus 0 pe pozitia", move, "!")
                print_Board(board)
        else:
            print("Ai castigat!!")
            break

    if board_Full(board):
        print("Egalitate!")


while True:
    answer = input("Joc nou? (D/N)")
    if answer.lower() == "d" or answer.lower == "da":
        board = [" " for i in range(10)]
        print("-------------------")
        program()
    else:
        break
