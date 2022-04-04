# create a simple dice game that will allow user to select number of players, how many sides on dice, and how many rounds.
# there will be two functions; one that rolls dice, and one that plays the game.
from collections import defaultdict
import array
import random


def playGame(p, r, n, s):
    # where p is the number of players
    # where r is the number of rounds
    # where n is number of dice
    # where s is number of sides on each die

    scores = []

    def rollDice(a, b):
        # function that returns score of a dice roll
        # where a is the number of dice
        # where b is the number of sides on dice
        score = 0
        sides = b
        for i in range(a):
            score = score + random.randint(1, sides)

        return score

    for i in range(r):
        # for each round create a new array for each players score for that round
        roundScores = []
        for j in range(p):
            # for each player in each round have them roll dice and push the score into the round score array
            # each players score in array will correspond to the players index in iteration
            # player 1s scores will always be at roundScores[0] and so on
            roundScores.append(rollDice(n, s))

        scores.append(roundScores)

    

    print(scores)
