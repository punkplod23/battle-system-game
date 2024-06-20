from game.dto import attributes
from game.dto import character
from game.entities import countdowntimer
from game.entities.gemeobject import gameObject 
import random
import string
import time

gameQue = []

def getGameObjectByPosition(i):
    return gameQue[i].getCharacter();

def printCharacter(i):
    print(
        "Enemy:",getGameObjectByPosition(i).name,"\n",
        "HP:",healthBar(getGameObjectByPosition(i).attributes.hp),"\n",
        "MP:",healthBar(getGameObjectByPosition(i).attributes.mp),"\n"
    )

def printEnemies():
    for i in range(len(gameQue)):
        if getGameObjectByPosition(i).type == "ENEMY":
            printCharacter(i)

def healthBar(value):
    bar = ""
    if value > 0:
        bar = "-"  * value
    minus = " " * (100-value)  
    bar = bar+minus  
    return "|"+bar+"|";
           
def setup():
    global gameRunning
    gameRunning = True
    gameQue.append(createHero());
    for i in range(random.randint(1,2)):
        gameQue.append(createEnemy());
    print("Welcome Hero \n")  
    printCharacter(0)
    print("Enemies Have Appeared \n")
    print(gameQue)
    printEnemies()
    runGame()

def checkConditions():
    countEntities = len(gameQue)
    if countEntities <= 1:
       print("All Enemies Defeated")
       return False 

    if getGameObjectByPosition(0).attributes.hp < 1:
        print("You Died")
        return False 
        
    return True 

def resetTimer(position):
    gameQue[position].timerCurrent = countdown(gameQue[position].timer)

def getLowestPosition():
    object_position = -99
    for i in range(len(gameQue)):
        if gameQue[i].checkIsTimerZero:
            return i
    return object_position     
            
              
def runQue():  
    position = getLowestPosition()
    if position != -99:
        object = getGameObjectByPosition(position);
        if object.type == "ENEMY":
            EnemyAttack(position); 
        
        if object.type == "HERO":
            HeroAttack();   
       
    time.sleep(1)

def FindEnemyPositionByName(name):
    for i in range(len(gameQue)):
        if getGameObjectByPosition(i).type == "ENEMY":
            if getGameObjectByPosition(i).name == name:
                return i   

def HeroAttack():
   printEnemies()
   personToAttack = input("Which Enemy would you like to attack:")
   position = FindEnemyPositionByName(personToAttack)
   
   if position:
   
    enemy = getGameObjectByPosition(position);
    if hitMiss(0):
        damage = attackOption(0)
        print("Hero:",enemy.name," inflicted\n",damage," damage")
        gameQue[position].characterObj.attributes.hp = enemy.attributes.hp-damage
      
        if gameQue[position].characterObj.attributes.hp < 1:
            print(enemy.name,"Is Dead")
            gameQue.remove(gameQue[position])
        else:
            printCharacter(position)
         
        printEnemies()   
        gameQue[0].resetTimer()
    else:
        print("Hero has missed",getGameObjectByPosition(position).name,"Has Missed\n",) 
        gameQue[0].resetTimer()  
   else:
       HeroAttack()
                 

    
def EnemyAttack(position):
    
    enemy = getGameObjectByPosition(position);
    print("Enemy:",getGameObjectByPosition(position).name,"Is Attacking\n",)
    if hitMiss(1):
        damage = attackOption(1)
        print("Enemy:",getGameObjectByPosition(position).name,"Has inflicted\n",damage," damage")
        gameQue[0].characterObj.attributes.hp = getGameObjectByPosition(0).attributes.hp-damage
        gameQue[position].resetTimer()
        printCharacter(0)
    else:
        gameQue[position].resetTimer()
        print("Enemy:",getGameObjectByPosition(position).name,"Has Missed\n",)
    
def runGame():
    while(checkConditions()):
      runQue()

def run():
   setup()
   

def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      

def hitMiss(isEnemy):
    hitOption = list(range(0,random.randint(1,22)))

    if isEnemy:
        hitOption = list(range(0,random.randint(1,11)))
            
    selectHitOption = hitOption[random.randint(0,len(hitOption)-1)]
    
    if selectHitOption == 0:
        return False;

    return selectHitOption % 2 == 0;
    
        
def attackOption(isEnemy):
    #Todo Modify based on mp
    hitDamaage = random.randint(1,55)
    if isEnemy:
       hitDamaage = random.randint(1,30)
    return hitDamaage
       
        
def randomName(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    
def createHero():
    
    attr = attributes.Attributes(100,100)
    obj = gameObject(5,character.Character(
        "HERO",
         0,
         "Hero",
         attr,
         "HERO"
    )) 
    
    obj.resetTimer()
    return obj
    
def createEnemy():
    tag = randomName()
    enemyName = "Enemy "+tag
    attr = attributes.Attributes(hp=random.randint(1,100),mp=random.randint(5,100))
    obj = gameObject(random.randint(30,60),character.Character(
        "ENEMY",
        0,
        enemyName,
        attr,
        "HERO",
        tag
    ))
    obj.resetTimer()
    return obj 



    

