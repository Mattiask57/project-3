# ------- Global Variables -------

board = {0: "-", 1: "-", 2: "-",
         3: "-", 4: "-", 5: "-",
         6: "-", 7: "-", 8: "-"}

game_running = True

current_player = "X"

# ------ Functions --------

def run_game():

    """
    Running the game
    """

def display_board(board):
    """
    Display board
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
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
                    display_board()
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
print("Top left = 1 and bottom right = 9. Choose a number to place your mark.")
print("\n_ _ _")
print("_ _ _")
print("_ _ _\n")
run_game()