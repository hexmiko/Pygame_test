from abc import ABC, abstractmethod
from pygame.surface import Surface


class GameObject(ABC):

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.image = None

    @abstractmethod
    def draw(self, tela: Surface):
        """abstractmethod"""

        raise Exception("Method not implemented")


    @abstractmethod
    def get_mask(self):
        """abstractmethod"""

        raise Exception("Method not implemented")
    

    def check_collision(self, object):
        pass