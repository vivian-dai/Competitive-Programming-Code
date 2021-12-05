def mark_board(board, number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = None

def check_win(board):
    for i in range(5):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == None:
            return True
        elif board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == None:
            return True
    return False

def check_last(boards_won):
    false_count = 0
    for won in boards_won:
        if not won:
            false_count += 1
    return True if false_count == 0 else False

with open("Advent of Code/2021/Day 4/input.txt") as inp:
    content = inp.read().splitlines()
    numbers = list(map(int, content[0].split(",")))
    boards = []
    board = []
    board_won = []
    for i in range(2, len(content)):
        if content[i] == "":
            boards.append(board)
            board_won.append(False)
            board = []
        else:
            board.append(list(map(int, content[i].strip().split())))
    board_won.append(False)
    boards.append(board)
    for number in numbers:
        for i in range(len(boards)):
            board = boards[i]
            mark_board(board, number)
            if check_win(board):
                board_won[i] = True
            if check_last(board_won):
                board_sum = 0
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] is not None:
                            board_sum += board[i][j]
                print(board_sum*number)
                exit()
