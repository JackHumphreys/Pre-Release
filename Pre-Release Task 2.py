# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment
import pdb

BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")


def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R{0}".format(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("      F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if StartRank == 7:
      if FinishRank == StartRank - 1 or FinishRank == StartRank - 2:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
            CheckRedumMoveIsLegal = True
    elif FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif ColourOfPiece == "B":
    if StartRank == 2:
      if FinishRank == StartRank + 1 or FinishRank == StartRank + 2:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
            CheckRedumMoveIsLegal = True
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  FileDifference = abs(FinishFile - StartFile)
  RankDifference = abs(FinishRank - StartRank)
  if FileDifference == RankDifference:
    CheckNabuMoveIsLegal = True
    if StartFile < FinishFile and StartRank > FinishRank:
       for count in range(1, RankDifference + 1):
         if Board[StartRank - count][StartFile + count] != "  ":
           CheckNabuMoveIsLegal = False
    elif StartFile > FinishFile and StartRank > FinishRank:
       for count in range(1, RankDifference + 1):
         if Board[StartRank - count][StartFile - count] != "  ":
           CheckNabuMoveIsLegal = False

  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 1):
    CheckMarzazPaniMoveIsLegal = True
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2) :
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if 0 > FinishFile > BOARDDIMENSION or 0 > FinishRank > BOARDDIMENSION:
    MoveIsLegal = False
  elif (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, selection, KashshaptuActivated): 
    if selection == 3: 
      InitialiseSampleBoard(Board)
    else:
      InitialiseNewBoard(Board, KashshaptuActivated)                        

def InitialiseNewBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      if RankNo == 2:
        Board[RankNo][FileNo] = "BR"
      elif RankNo == 7:
        Board[RankNo][FileNo] = "WR"
      elif RankNo == 1 or RankNo == 8:
        if RankNo == 1:
          Board[RankNo][FileNo] = "B"
        if RankNo == 8:
          Board[RankNo][FileNo] = "W"
        if FileNo == 1 or FileNo == 8:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
        elif FileNo == 2 or FileNo == 7:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
        elif FileNo == 3 or FileNo == 6:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
        elif FileNo == 4:
          if Board[RankNo][FileNo] == "B": 
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
          else:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
        elif FileNo == 5:
          if Board[RankNo][FileNo] == "B": 
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          else:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
      else:
        Board[RankNo][FileNo] = "  "

def InitialiseSampleBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"
                 
def GetMove(StartSquare, FinishSquare, WhoseTurn):
  correct = False
  while not correct:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first) or type '-1' for menu: "))
      if StartSquare == -1:
        display_pause_menu()
        pause_selection = get_pause_menu_selection(WhoseTurn)
      StartSquareString = str(StartSquare)
      while len(StartSquareString) > 2 or StartSquareString == "-1":
        print("Please provide both FILE and RANK for this move.")
        StartSquare = int(input("Enter coordinates of square containing piece to move (file first) or type '-1' for menu: "))
        StartSquareString = str(StartSquare)
      correct = True
    except ValueError:
      print("Error! Please enter a valid integer.")
  correct2 = False
  while not correct2:
    try:  
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      FinishSquareString = str(FinishSquare)
      while len(FinishSquareString) != 2:
        print("Please provide both FILE and RANK for this move.")
        FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
        FinishSquareString = str(FinishSquare)
      correct2 = True
    except ValueError:
      print("Error! Please enter a valid integer.")
  return StartSquare, FinishSquare


def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
    if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
        Board[FinishRank][FinishFile] = "WM"
        ColourStart, TypeStart, ColourFinish, TypeFinish = GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile)
        print("{0} Redum promoted to Marzaz Pani.".format(ColourStart))
        Board[StartRank][StartFile] = "  "  
    elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
        Board[FinishRank][FinishFile] = "BM"
        ColourStart, TypeStart, ColourFinish, TypeFinish = GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile)
        print("{0} Redum promoted to Marzaz Pani.".format(ColourStart))
        Board[StartRank][StartFile] = "  "
    elif Board[FinishRank][FinishFile] != "  ":
        ColourStart, TypeStart, ColourFinish, TypeFinish = GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile)
        print("{0} {1} takes {2} {3}.".format(ColourStart, TypeStart, ColourFinish, TypeFinish))
        Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
        Board[StartRank][StartFile] = "  "
    else:
        Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
        Board[StartRank][StartFile] = "  "
        

def ConfirmMove(StartSquare, FinishSquare):
  StartRank = StartSquare % 10
  StartFile = StartSquare // 10
  FinishRank = FinishSquare % 10
  FinishFile = FinishSquare // 10
  print()
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartRank, StartFile, FinishRank, FinishFile))
  Confirmation = input("Comfirm move (Yes/No): ")
  print()
  ConfirmationList = ["y","Y","Yes","yes","n","N","No","no"]
  ConfirmationYes = ["y","Y","Yes","yes"]
  ConfirmationNo = ["n","N","No","no"]
  while Confirmation not in ConfirmationList:
    print()
    print("Your input is not valid. Try again:")
    print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartRank, StartFile, FinishRank, FinishFile))
    Confirmation = input("Comfirm move (Yes/No): ")
  if Confirmation in ConfirmationYes:
    ConfirmationBoolean = True
  elif Confirmation in ConfirmationNo:
    ConfirmationBoolean = False
  return ConfirmationBoolean

def GetPieceName(Board, StartRank, StartFile, FinishRank, FinishFile):
  PieceTypeStart = Board[StartRank][StartFile][1]
  PieceColourStart = Board[StartRank][StartFile][0]
  if PieceColourStart == "W":
    ColourStart = "White"
  else:
    ColourStart = "Black"
  if PieceTypeStart == "R":
    TypeStart = "Redum"
  elif PieceTypeStart == "G":
    TypeStart = "Gisgigir"
  elif PieceTypeStart == "E":
    TypeStart = "Etlu"
  elif PieceTypeStart == "N":
    TypeStart = "Nabu"
  elif PieceTypeStart == "M":
    TypeStart = "Marzaz pani"
  elif PieceTypeStart == "S":
    TypeStart = "Sarrum"
  PieceTypeFinish = Board[FinishRank][FinishFile][1]
  PieceColourFinish = Board[FinishRank][FinishFile][0]
  if PieceColourFinish == "W":
    ColourFinish = "White"
  else:
    ColourFinish = "Black"
  if PieceTypeFinish == "R":
    TypeFinish = "Redum"
  elif PieceTypeFinish == "G":
    TypeFinish = "Gisgigir"
  elif PieceTypeFinish == "E":
    TypeFinish = "Etlu"
  elif PieceTypeFinish == "N":
    TypeFinish = "Nabu"
  elif PieceTypeFinish == "M":
    TypeFinish = "Marzaz pani"
  elif PieceTypeFinish == "S":
    TypeFinish = "Sarrum"
  return ColourStart, TypeStart, ColourFinish, TypeFinish

def display_menu():
  print()
  print("MAIN MENU")
  print()
  print("1. Start new game")
  print("2. Load existing game")
  print("3. Play sample game")
  print("4. View high scores")
  print("5. Settings ")
  print("6. Quit program")
  print()

def get_menu_selection():
  selection = int(input("Select an option from the menu: "))
  while 1 > selection > 6:
    print("Your input is invalid. Try again.")
    selection = int(input("Select an option from the menu: "))
  return selection

def display_settings():
  print()
  print("1. Use Kashshaptu Piece")
  print("9. Return to Main Menu")
  print()

def get_settings_selection():
  settings_selection = int(input("Please select an option: "))
  while 1 != settings_selection != 9:
    print("Your input is invalid. Try again.")
    settings_selection = int(input("Please select an option: "))
  return settings_selection

def make_settings_selection(settings_selection):
  KashshaptuActivated = False
  if settings_selection == 1:
    kashshaptuConfirmation = input("Do you wish to use the kashshaptu piece (Y/N)?: ")
    AcceptList = ["Y", "N"]
    while kashshaptuConfirmation not in AcceptList:
      print()
      print("Your input is invalid. Try again.")
      print()
      kashshaptuConfirmation = input("Do you wish to use the kashshaptu piece (Y/N)?: ")
    if kashshaptuConfirmation == "N":
      StopSettingLoop = True
    else:
      print("Kashshaptu Activated")
      KashshaptuActivated = True
      StopSettingLoop = True
  elif settings_selection == 9:
    StopSettingLoop = True
  return StopSettingLoop, KashshaptuActivated
  

def display_pause_menu():
  print()
  print("Options")
  print()
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender")


def get_pause_menu_selection(WhoseTurn):
  print()
  pause_menu_selection = int(input("Please select an option: "))
  while pause_menu_selection > 4 or pause_menu_selection < 1:
    print("Your input is invalid. Try again.")
    pause_menu_selection = int(input("Please select an option: "))
  if pause_menu_selection == 1:
    print("Save successful.")
  elif pause_menu_selection == 2:
    main_menu()
  elif pause_menu_selection == 3:
    pass
  elif pause_menu_selection == 4:
    surrender(WhoseTurn)
  return pause_menu_selection

def surrender(WhoseTurn):
  print()
  print("Surrendering...")
  print()
  if WhoseTurn == "W":
    print("White surrendered. Black wins!")
  else:
    print("Black surrendered. White wins!")
  main_menu()

def play_game(selection, KashshaptuActivated):
    Board = CreateBoard() #0th index not used
    StartSquare = 0 
    FinishSquare = 0
    PlayAgain = "Y"
    while PlayAgain == "Y":
      WhoseTurn = "W"
      GameOver = False
      InitialiseBoard(Board, selection, KashshaptuActivated)
      while not(GameOver):
        DisplayBoard(Board)
        Turn = DisplayWhoseTurnItIs(WhoseTurn)
        MoveIsLegal = False
        while not(MoveIsLegal):
          StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare, WhoseTurn)
          ConfirmationBoolean = ConfirmMove(StartSquare, FinishSquare)
          while ConfirmationBoolean == False:
            StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare,WhoseTurn)
            ConfirmationBoolean = ConfirmMove(StartSquare, FinishSquare)
          StartRank = StartSquare % 10
          StartFile = StartSquare // 10
          FinishRank = FinishSquare % 10
          FinishFile = FinishSquare // 10
          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if not(MoveIsLegal):
            print("That is not a legal move - please try again")
        GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
        MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if GameOver:
          DisplayWinner(WhoseTurn)
        if WhoseTurn == "W":
          WhoseTurn = "B"
        else:
          WhoseTurn = "W"
      PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
      if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
        PlayAgain = chr(ord(PlayAgain) - 32)

def make_selection(selection):
    if selection == 1:
        play_game(selection, KashshaptuActivated)
    elif selection == 2:
      pass
    elif selection == 3:
        play_game(selection, KashshaptuActivated)
    elif selection == 4:
      pass
    elif selection == 5:
      StopSettingLoop = False
      while StopSettingLoop == False:
        display_settings()
        settings_selection = get_settings_selection()
        StopSettingLoop, KashshaptuActivated = make_settings_selection(settings_selection)
      StopMainMenuLoop = True
    elif selection == 6:
      quit()
    return StopMainMenuLoop


def main_menu():  
    Start = True
    while Start == True:
      StopMainMenuLoop = False
      while StopMainMenuLoop == False:
        display_menu()
        selection = get_menu_selection()    
        StopMainMenuLoop = make_selection(selection)
      StopMainMenuLoop = False
  


if __name__ == "__main__":
  main_menu()
