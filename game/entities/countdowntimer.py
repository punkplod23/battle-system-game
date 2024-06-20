import time
class countDownTimer:
    resetTimer = 0
    Timer = 0
    
    def __init__(self,time = 0):
        self.resetTimer = time
        self.Timer = time
        
    def countdown(self): 
        while self.Timer: 
            time.sleep(1) 
            self.Timer -= 1
    
    def resetTimer(self):
        self.Timer = self.resetTimer
            

    
    