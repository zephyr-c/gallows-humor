import random
def reveal_letters(s, w, g):
    for index in range(len(s)):
        if s[index] == g:
            w[index] = g
    return w
def makeword(l):
    new = "".join(l)
    return new
gamefile = open("wordlist.txt", "r")
gamewords = gamefile.read()
gamefile.close()
gamewords = gamewords.splitlines()
artfile = open("hangart.txt", "r")
art = artfile.read()
artfile.close()
art = art.split(",")

while True:
    print("""
    Welcome to Hangman!
    Enter 'quit' at any time to quit the current round
    You get 10 mistakes before the man hangs
    If you think you know the whole word you can enter it at any time
    Have fun!
    """)
    source = gamewords[random.randint(0, len(gamewords)-1)]
    letters = ["*" for i in source]
    attempts = 0
    wrong = []
    while attempts<10:
        word = makeword(letters)
        print("The word is:", word)
        gus = str(input("Guess a letter: "))
        if gus == "quit":
            break
        if gus in wrong or gus in word:
            print("You already tried that.")
        elif gus.isalpha() == False:
            print("That's not a letter, try again.")
        elif len(gus) > 1 and len(gus) != len(source) and gus != source:
            print("That's too many letters")
        elif gus in source:
            letters = reveal_letters(source, letters, gus)
        elif gus not in source:
            print(art[attempts])
            attempts += 1
            wrong.append(gus)
#            print("Nope")
            print("Mistakes: ", wrong)

        if makeword(letters) == source or gus == source:
            print("You did it! The word is", source + "!")
            break
    if attempts == 10:
        print("Better luck next time partner. X__X")
        print("The word was", source)

    play = str(input("Play Again? Y/N? "))
    if play.upper() != "Y":
        print("Goodbye!")
        break
    else:
        continue
