class gameEn:

    def __init__(self, word):
        # Initialise
        self.word = list(word)
        self.shownWord = list(word)
        self.tIncGuess = 0
        self.nIncGuess = 0
        self.gLetter = []
        self.incLetter = []

        for l in range(0, len(self.shownWord)):
            self.shownWord[l] = '_'

        for l in range(0, len(self.word)):
            self.word[l] = self.word[l].lower()

        self.tIncGuess = len(word)
        if self.tIncGuess > 10:
            self.tIncGuess = 10

    def mainGameLoop(self):
        # Main loop goes here
        gameLoop = True
        while gameLoop:
            self.printHUD()
            while self.guessLetter(input("Please guess a letter\n")):
                print()
            if self.word == self.shownWord:
                gameLoop = False
                self.printWin()
            if self.tIncGuess == self.nIncGuess:
                gameLoop = False
                self.printLose()

    def guessLetter(self, letter):
        # Guess letter
        letter = letter.lower()

        if len(letter) > 1:
            return True

        if letter.isalpha():

            if letter in self.gLetter:
                return True
            else:
                self.gLetter.append(letter)
                self.proccesLetter(letter)
                return False

        else:
            return True

    def proccesLetter(self, letter):
        if letter in self.word:
            for i in range(0, len(self.word)):
                if self.word[i] == letter:
                    self.shownWord[i] = letter
        else:
            self.incLetter.append(letter)
            self.nIncGuess += 1

    def printWin(self):
        # Print winning message
        print("\033[1;33;40m" + "CONGRAGULATION! YOU ARE WINNER!" + "\033[1;37;40m")

    def printLose(self):
        print("\033[1;31;40m" + "YOU ARE THE LOSE" + "\033[1;37;40m")
        print("The correct word was: " + str(self.word) + ".")

    def printHUD(self):
        print('\n' * 100)
        print("SPACEMAN")
        temp = self.tIncGuess - self.nIncGuess
        print("Guesses left: " + str(temp) + "\n")
        print(str(self.shownWord) + "\n")
        print("Incorrect Guesses: " + str(self.incLetter))
        print("Total Guesses: " + str(self.gLetter))


game = gameEn("Apple")

game.mainGameLoop()
