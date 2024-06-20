import time
from game.entities import countdowntimer
from game.dto import character
from threading import Thread

class gameObject:
    characterObj = character.Character
    countdowntimer = countdowntimer
    timer_thread = Thread
    
    def __init__(self,time = 0,characterobj = character.Character):
        self.countdowntimer = countdowntimer.countDownTimer(time)
        self.characterObj = characterobj
      
    def checkIsTimerZero(self):
        if self.countdowntimer.Timer <= 0:   
           return True  
       
    def resetTimer(self):
        self.countdowntimer.resetTimer
        self.timer_thread = Thread(target=self.countdowntimer.countdown, daemon = True)
        self.timer_thread.start()
        
    def getCharacter(self):
        return self.characterObj   
           
