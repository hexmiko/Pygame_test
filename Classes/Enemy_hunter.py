from Classes import Enemy
from interfaces.gameObject import GameObject


class Hunter(Enemy):

    def __init__(self,x,y, target) -> None:

        super().__init__(x,y)
        ###self.velocity = self.velocity
        self.target = target


    def mover(self):
        if self.y - 10 > self.target.y:
            self.y -= self.velocity/2

        elif self.y + 10 < self.target.y:
            self.y += self.velocity/2
        
        else:
            self.velocity += self.velocity / 100

        return super().mover()


    def draw(self, tela):
        return super().draw(tela)


    def get_mask(self):
        return super().get_mask()


    def check_collision(self, object: GameObject):
        return super().check_collision(object)
