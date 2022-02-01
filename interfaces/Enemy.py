from abc import abstractmethod
from pygame import Surface
from interfaces import GameObject

class EnemyInterface(GameObject):
    
    def __init__(self, x=0, y=0) -> None:
        super().__init__(x, y)
    
    @abstractmethod
    def draw(self, tela: Surface):
        return super().draw(tela)
    
    @abstractmethod
    def check_collision(self, object):
        return super().check_collision(object)

    @abstractmethod
    def mover(self):
        pass
