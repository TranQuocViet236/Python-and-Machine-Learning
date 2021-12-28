# ------------------------------
def newGame():
    guesses =[]
    correctGuesses = 0
    questionNum = 1
    for key in question:
        print("------------------------------")
        print(key)
        for i in options[questionNum - 1]:
            print(i)
        guess = input("You answer: (A,B,C,D)")
        guess = guess.upper()
        guesses.append(guess)
        correctGuesses += checkAnswer(question.get(key), guess)
        questionNum +=1
    displayScore(correctGuesses, guesses)
    # playAgain()
# ------------------------------
def checkAnswer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# ------------------------------
def displayScore(correcctGuesses, guesses):
        print("Your answer: ")
        for i in guesses:
            print(i, end=" ")
        print()
        print("Correct answer: ")
        for i in question:
            print(question.get(i), end=" ")
        print()
        score = int((correcctGuesses / len(question)) * 100)
        print("Your score: "+ str(score)+"%")
# ------------------------------
def playAgain():
        respon = input("Do you want to play again?(Yes/No)")
        respon = respon.lower()
        if respon != "yes":
            return False
        else:
            return True
# ------------------------------
question = {
    "Who create Python?": "A",
    "What year was Python created?": "B",
    "Is Python tributed to which comedy group?": "C",
    "Is the Earth around?": "A"
}
options = [
    ["A. Guido van Rossum", "B. Leonel Messi", "C. Cristiano Ronaldo", "D. Segio Aguero"],
    ["A. 1989", "B. 1991", "C. 1993", " D.1995"],
    ["A. Barcalona", "B. Real Madrid", "C. Monty Python", "D. SNL"],
    ["A. True", "B.False", "C. What", "D.How"]
]
newGame()
while(playAgain()):
    newGame()
