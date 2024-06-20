from dataclasses import dataclass
from game.dto import attributes
@dataclass
class Character():
    type: str
    position: int
    name: str
    attributes: attributes.Attributes
    action: str = "Prone"
    playedTurn: bool = False
    target: str = "HERO"
    tag: str = "HERO"
    envokeAction: bool = False
    


      
   
    
