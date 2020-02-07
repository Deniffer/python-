# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:44:46 2019

@author: HASEE
"""

import random
class Player():
    def __init__(self):
        self.score=0
        self.numberOfgames=0
        self.wins=0
        self.name=""
    def getName(self):
        self.name=input("name:")
        return self.name

    def updateNumberOfGames(self):
        self.numberOfgames+=1
    def updateScore(self):
        self.score+=self.score
    def updateWins(self):
        self.wins+=1

class MasterMindGame():
    def __init__ (self):
        self.code=[]
        self.guess=""
        self.game=True
        self.caseLevel=0
        self.case=["intro","playing","codecracked","exit"]
        self.attempt=0
    def initGame(self):
        self.code=[]
        x=[0,1,2,3,4,5,6,7]
        for i in range(self.caseLevel+4):
            self.code.append(random.choice(x))
        
    def dispalyRules(self):
        pass
    def askForNumber(self):
        number=int(input("  [0] Detective [1] Inspector [2] Chief Inspector : "))
        if number==0 or number==1 or number==2:
            self.caseLevel=number
        else:
            print("invalid input please input again!")
            self.askForNumber()
    def inputNumber(self):
        self.guess=input("please input guess number:")
    #def askForLetter(self):
    def compare(self):
        self.guess=self.guess.split(" ")
        guess_list=[]
        good_guess=0
        for i in range(len(self.code)):
            if eval(self.guess[i])==self.code[i]:
                guess_list.append("。")
                good_guess+=1
            elif eval(self.guess[i]) in self.code:
                guess_list.append("?")
            else:
                guess_list.append("*")
        print(guess_list)
        #print(self.code)
        return good_guess
        
    def playGame(self):
        print("Good luck cracking the code!\n\n")
        self.attempt=1
        playing=True
        while(playing):
            print("ROUND - %i :\n"%self.attempt)
            print("use space to split your input(4 or 5 or 6 depending your caseLevel)number,use Enter to end your input(eg:1 2 3 4 5 6)\n")
            self.inputNumber()
            if self.compare()==(self.caseLevel+4):
                playing=False                
            self.attempt+=1
        #return attempt
    def displayResults(self):
        print("Name:%s"%myplayer.name)        
        if self.caseLevel==0:
            rank="Detective"
        elif self.caseLevel==1:
            rank="Inspector"
        else:
            rank="Chief Inspector"
        print("Rank: %s"%rank)
        #print("Round: %i"%self.playGame())
        print("sloved: %i"%myplayer.wins)

    def gameOver(self):
        print("Congratulation, it takes you %i Round to solve the puzzle!"%self.attempt)
    def resetGame(self):
        letter = input("Are you ready for your next cases? (y/n):")
        if letter=="y"or letter=="Y":
            return True
        else:
            self.game=False
            return False
class board():
    def __init__ (self):
        pass

    def dispalyBoard(self,file):
        with open(file,mode="r")as f:
            for i in f:
                print(i)

if __name__ == '__main__':
    myplayer=Player()
    mygame=MasterMindGame()
    myboard=board()
    #game=True
    gamestate=mygame.case[0]
    while(mygame.game):
        if gamestate=="intro":
            myboard.dispalyBoard("Text.txt")
            x=input("")
            myboard.dispalyBoard("Text1.txt")
            myplayer.getName()
            myboard.dispalyBoard("Text2.txt")
            mygame.askForNumber()
            print("Thanks,Detective%s.Good luck with your cases!"%myplayer.name)
            mygame.displayResults()
            gamestate=mygame.case[1]
        elif gamestate=="playing":
            mygame.initGame()
            mygame.playGame()
            gamestate="codecracked"
        elif gamestate=="codecracked":
            myplayer.updateNumberOfGames()
            myplayer.updateWins()
            mygame.gameOver()
            mygame.displayResults()
            gamestate="exit"
        elif gamestate=="exit":
            if mygame.resetGame()==True:
                gamestate="playing"
            else:
                mygame.game=False
