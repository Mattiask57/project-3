# ------- Global Variables -------

board = {0: "-", 1: "-", 2: "-",
         3: "-", 4: "-", 5: "-",
         6: "-", 7: "-", 8: "-"}

game_running = True

current_player = "X"

winner = None
# ------- Classes -------
class Error(Exception):
    """
    Class for exceptions
    """
    pass


class SpaceTakenError(Error):
    """
    Runing when space already taken
    """
    pass

# ------ Functions --------

def check_win():
    """
    All possible winning combinations.
    """
    if (board[1] == board[2] and board[1] == board[3] and board[1] != "-"):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != "-"):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != "-"):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != "-"):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != "-"):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != "-"):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != "-"):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != "-"):
        return True
    else:
        return False

def check_draw():
    """
    Check if game is draw
    """
    for key in board.keys():
        if board[key] == "-":
            return False

    return True

def check_if_game_over():
    """ Check if win or draw """
    check_win()
    check_draw()

def flip_player():
    """ Swaps the current player """
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def run_game():

    """
    Running the game
    """
    display_board(board)

        while game_running:

        handle_turn(current_player)
        check_if_game_over()
        swap_player()
        if winner == "X" or winner == "O":
            print(winner + "wins!")
            exit()

def display_board(board):
    """
    Display board
    """
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("\n")

    def handle_turn(player):
    """
    Handles player turns and checks valid input.
    """
    print(player + "'s turn.")
    valid = False
    position = input("\nChoose a position from 1-9: ")
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while not valid:
        try:
            if position not in x:
                raise ValueError
            else:
                position = int(position) - 1
                if board[position] == "-":
                    valid = True
                    board[position] = player
                    display_board(board)
                    return
                else:
                    raise SpaceTakenError
        except ValueError:
            print("\nError: Incorrect Value Please Try Again\n")
            position = input("\nChoose a position from 1-9: ")
        except SpaceTakenError:
            print("\nError: Space Taken, Try Again\n")
            position = input("\nChoose a position from 1-9: ")




    """
    Welcome message
    """
print("\nWelcome to the best tic-tack-toe game out there!\n")
print("How to play: \n")
print("You will use a mark (X or O) and place it on the board.")
print("First one to place three marks in a row wins.")
print("These underscores is the board positions.")
print("Top left = 0 and bottom right = 8. Choose a number to place your mark.")
print("\n_ _ _")
print("_ _ _")
print("_ _ _\n")
run_game()