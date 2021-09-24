loop = 30
whileloop = ["Rock", "rock", "ROck", "ROCk", "ROCK", "rOCK", "roCK", "rocK", "Paper", "paper", "PAper", "PAPer", "PAPEr", "PAPER", "pAPER", "paPER", "papER", "papeR", "Scissors", "scissors", "SCissors","SCIssors","SCISsors","SCISSors","SCISSOrs","SCISSORs", "SCISSORS"]
for i in range(loop):
  player = input("\nRock, Paper Or Scissors?:")
  if player not in whileloop:
      print("invalid entry please try again")
      loop = loop+1
  elif player in whileloop:

      for i in range(50):
       print("\n")
      player2 = input("\nRock,Paper Or Scissors?:")
      if player in ["Rock", "rock", "ROck", "ROCk", "ROCK", "rOCK", "roCK", "rocK"]:
          if player2 in ["Rock", "rock", "ROck", "ROCk", "ROCK", "rOCK", "roCK", "rocK"]:
              print("Draw!")
          elif player2 in ["Scissors", "scissors", "SCissors","SCIssors","SCISsors","SCISSors","SCISSOrs","SCISSORs", "SCISSORS"]:
              print("Player 1 won!")
          else:
              print("Player 2 won!")
      if player in ["Paper", "paper", "PAper", "PAPer", "PAPEr", "PAPER", "pAPER", "paPER", "papER", "papeR"]:
          if player2 in ["Paper", "paper", "PAper", "PAPer", "PAPEr", "PAPER", "pAPER", "paPER", "papER", "papeR"]:
              print("Draw!")
          elif player2 in ["Rock", "rock", "ROck", "ROCk", "ROCK", "rOCK", "roCK", "rocK"]:
              print("player 1 won!!")
          else:
              print("Player 2 won!")
      if player in ["Scissors", "scissors", "SCissors","SCIssors","SCISsors","SCISSors","SCISSOrs","SCISSORs", "SCISSORS"]:

          if player2 in ["Scissors", "scissors", "SCissors","SCIssors","SCISsors","SCISSors","SCISSOrs","SCISSORs", "SCISSORS"]:
              print("Draw!")
          elif player2 in ["Paper", "paper", "PAper", "PAPer", "PAPEr", "PAPER", "pAPER", "paPER", "papER", "papeR"]:
              print("player 1 won!!")
          else:
              print("player 2 won!")

player1wins = input("How many times did player 1 win?:")
player2wins = input("How many times did player 2 win?:")
if player2wins >= player1wins:
   print("PLAYER 2 WINS!!!!!!!")
else:
   print("PLAYER 1 WINS!!!!!!!")
