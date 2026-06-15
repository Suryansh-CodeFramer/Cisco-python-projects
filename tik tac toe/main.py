import random

board=[
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]
def display_board(board):
    line="+-----+-----+-----+"
    for row in board:
        print(line)
        print("|       |       |       |")
        print(f"|    {row[0]}  |    {row[1]}  |    {row[2]}  |")
        print("|       |       |       |")
    print("+-----+-----+-----+")


display_board(board)

def make_list_of_free(board):
    free =[]
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ("X", "O"):
                free.append((r,c))
    return free


def victory_for(board, sign):
    for i in range(3):
        if all(board[i][c]==sign for c in range(3)):
            return True
        if all(board[r][i] == sign for r in range(3)):
            return True
    if all(board[i][2 - i] == sign
           for i in range(3)):
        return True
    if all(board[i][i] == sign for i in range(3)):
        return True
    return False
def enter_move(board):
    free = make_list_of_free(board)
    while True:
        try:
            move=int(input("enter the move:"))

        except ValueError:
            print("enter a number!")
            continue
        if move<1 or move>9:
            print("Must be 1 to 9")
            continue
        row,col=(move-1)//3,(move-1)%3
        if (row,col) not in free:
            print("that square is taken!")
            continue
        board[row][col]="O"
        break
def draw_move(board):
    free = make_list_of_free(board)
    if free:
        row,col=free[random.randrange(len(free))]
        board[row][col] = 'X'

board[1][1] = 'X'
display_board(board)




while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("You win!")
        break
    if not make_list_of_free(board):
        print("its a tie")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("Computer win!")
        break
    if not make_list_of_free(board):
        print("its a tie")
        break

