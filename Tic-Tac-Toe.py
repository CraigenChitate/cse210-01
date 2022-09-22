
'''
Tic-Tac-Toe: Game
Author: Craigen Chitate
'''



def main():
    playing = player_turn("")
    new_board = board()

    while not (winner(new_board) or draw(new_board)):
        display(new_board)
        move_player(playing, new_board)
        playing = player_turn(playing)
    display(new_board)
    print("\nGood game!! Thanks  for playing!")

def board():
    board = []
    for new_place in range(9):
        board.append(new_place + 1)
    return board

def display(board):
    print("\n %s | %s | %s" %(board[0], board[1], board[2]))
    print('---+---+---')
    print(" %s | %s | %s" %(board[3], board[4], board[5]))
    print('---+---+---')
    print(" %s | %s | %s" %(board[6], board[7], board[8]))

def winner(board):
    return (board[0] == board[1]== board[2] or 
            board[3] == board[4] == board[5] or 
            board[6] == board[7] == board[8] or 
            board[0] == board[3] == board[6] or 
            board[1] == board[4] == board[7] or 
            board[2] == board[5] == board[8] or 
            board[2] == board[4] == board[6] or 
            board[0] == board[4] == board[8])

def draw(board):
    for new_place in range(9):
        if board[new_place] != "x" and board[new_place] != "o":
            return False
    return True 


def move_player(player, board):
    new_place = int(input(f"\n{player}'s turn to choose a new_place (1-9): "))
    board[new_place - 1] = player

def player_turn(turn):
    if turn == "" or turn == "o":
        return "x"
    elif turn == "x":
        return "o"

if __name__ == "__main__":
    main()