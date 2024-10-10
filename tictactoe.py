import random
def tictactoe():

    # Function to print the Tic Tac Toe board
    def printBoard(board): #print the tictactoe board
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    # Function to check if the board is full
    def isBoardFull(board):
        return all([spot != " " for spot in board])

    # Function to check for a win
    def seeIfWon(board, mark): # all possible combinations to win
        winner = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(board[i] == mark for i in condition) for condition in winner)

    # Function for player's turn
    def playerTurn(board): #players turn
        move = -1
        while move not in range(1, 10) or board[move - 1] != " ":
            try:
                move = int(input("Choose your move (1-9): "))
                if board[move - 1] != " ":
                    print("That space is already taken. Please choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Please choose a number from 1 to 9.")
        return move - 1

    # Function for NPC's turn
    def npcTurn(board):
        available_spots = [i for i, spot in enumerate(board) if spot == " "]
        return random.choice(available_spots)

    # Game initialization
    board = [" "] * 9
    currentTurn = "Player"

    # Main game loop
    while True:
        printBoard(board)
        if currentTurn == "Player": #player is X's
            index = playerTurn(board)
            board[index] = "X"
            if seeIfWon(board, "X"): #see if player wins
                printBoard(board)
                return "You won! You know, a weird life form was just in here, you might want to get ready for a fight."
            currentTurn = "NPC"
        else:
            print("NPC's turn...")
            index = npcTurn(board)
            board[index] = "O"                   #NPC is O's
            if seeIfWon(board, "O"):
                printBoard(board)
                return "NPC wins!"
            currentTurn = "Player"

        if isBoardFull(board): #full board and no winner = tue
            printBoard(board)
            return "It's a tie!"

