def mark_board(board, number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = None

def check_win(board):
    # if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == None:
    #     return True
    # elif board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] == None:
    #     return True
    # else:
    for i in range(5):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == None:
            return True
        elif board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == None:
            return True
    return False
    
with open("Advent of Code/2021/Day 4/input.txt") as inp:
    content = inp.read().splitlines()
    numbers = list(map(int, content[0].split(",")))
    boards = []
    board = []
    # print(content)
    for i in range(2, len(content)):
        if content[i] == "":
            boards.append(board)
            board = []
        else:
            board.append(list(map(int, content[i].strip().split())))
    boards.append(board)
    for number in numbers:
        for board in boards:
            mark_board(board, number)
            if check_win(board):
                board_sum = 0
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] is not None:
                            board_sum += board[i][j]
                print(board_sum*number)
                exit()