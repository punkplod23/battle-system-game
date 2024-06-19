from game.dto import attributes
from game.dto import character
import random
import string
import time

gameQue = [] #[character.Character]
firstRun = 0
highest_position = 12333333333333
    
def printCharacter(i):
    print(
        "Enemy:",gameQue[i].name,"\n",
        "HP:",healthBar(gameQue[i].attributes.hp),"\n",
        "MP:",healthBar(gameQue[i].attributes.mp),"\n"
    )

def printEnemies():
    for i in range(len(gameQue)):
        if gameQue[i].type == "ENEMY":
            printCharacter(i)

def healthBar(value):
    color_red = "\033[91m"
    color_green = "\033[92m"
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
    enemyActionChange()
    attributePositions()
    print("Enemies Have Appeared \n")
    printEnemies()
    runGame()

def checkConditions():
    countEntities = len(gameQue)
    if countEntities <= 1:
       print("All Enemies Defeated")
       return False 

    for i in range(len(gameQue)):
        if gameQue[i].type == "HERO":
            if gameQue[i].attributes.hp < 1:
                print("You Died")
                return False 
        
    return True 

def getLowestPosition():

    object_position = -99
    for i in range(len(gameQue)):
        if highest_position  > gameQue[i].position:
            object_position = i       
    
    if object_position == -99:
        attributePositions()
        return getLowestPosition()
    
        
    return object_position     
            
              
def runQue():  
    position = getLowestPosition()

    object = gameQue[position];

        

    if object.type == "ENEMY":
       EnemyAttack(position); 
       
    if object.type == "HERO":
       HeroAttack();   
       
    time.sleep(1)

def FindEnemyPositionByName(name):
    for i in range(len(gameQue)):
        if gameQue[i].type == "ENEMY":
            if gameQue[i].name == name:
                return i   

def HeroAttack():
   printEnemies()
   personToAttack = input("Which Enemy would you like to attack:")
   position = FindEnemyPositionByName(personToAttack)
   
   if position:
   
    enemy = gameQue[position];
    if hitMiss(0):
        damage = attackOption(0)
        print("Hero:",enemy.name," inflicted\n",damage," damage")
        gameQue[position].attributes.hp = enemy.attributes.hp-damage
      
        if gameQue[position].attributes.hp < 1:
            print(enemy.name,"Is Dead")
            gameQue.remove(enemy)
        else:
            printCharacter(position)
         
        printEnemies()   
        gameQue[0].position = highest_position
    else:
        print("Hero has missed",gameQue[position].name,"Has Missed\n",)   
        gameQue[0].position = highest_position
   else:
       HeroAttack()
                 

    
def EnemyAttack(position):
    
    enemy = gameQue[position];
    print("Enemy:",gameQue[position].name,"Is Attacking\n",)
    if hitMiss(1):
        damage = attackOption(1)
        print("Enemy:",gameQue[position].name,"Has inflicted\n",damage," damage")
        gameQue[0].attributes.hp = gameQue[0].attributes.hp-damage
        printCharacter(0)
        gameQue[position].position = highest_position
    else:
        gameQue[position].position = highest_position
        print("Enemy:",gameQue[position].name,"Has Missed\n",)
    
def runGame():
    while(checkConditions()):
      runQue()

def run():
   setup()
   

def hitMiss(isEnemy):
    hitOption = list(range(0,random.randint(1,2)))

    if isEnemy:
        hitOption = list(range(0,random.randint(1,6)))
            
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
     return character.Character(
        "HERO",
         0,
         "Hero",
         attr,
         "ENEMY"
    )
    
def createEnemy():
    tag = randomName()
    enemyName = "Enemy "+tag
    attr = attributes.Attributes(hp=random.randint(1,100),mp=random.randint(1,100))
    return character.Character(
        "ENEMY",
        0,
        enemyName,
        attr,
        "HERO",
        tag
    )

def getActionsOptions():
    actions = ('ATTACK', 'DEFEND', 'PRONE')
    return actions

def getRandomAction():
      action = getActionsOptions()[random.randint(0,2)]
      return action

def attributePositions():
    positions = list(range(0,len(gameQue)))
    random.shuffle(positions)
    for i in range(len(gameQue)):
        gameQue[i].position = positions[i]
    

def enemyActionChange():
    for i in range(len(gameQue)):
        gameQue[i].action = getRandomAction()