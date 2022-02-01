from random import randrange
from pygame import time


class Spawner:

    def __init__(self, x, y, objeto, listadeobjetos) -> None:
        self.x = x
        self.y = y
        self.objeto = objeto
        self.lista = listadeobjetos
        self.last_tick = 0


    def spawnar(self, spawn_cooldown=3) -> None:
        """
        Spawnar o objeto a cada x segundos nas coordenadas do spawner.
            params: spawn_cooldown - cooldown para spawnar
            return: None
        """

        if self.__cooldown(spawn_cooldown):
            self.lista.append(self.__create_object(self.objeto)) # add object to list

    def spawnar_hunter(self, target, spawn_cooldown=3) -> None:
        """
        Spawnar o objeto a cada x segundos nas coordenadas do spawner.
            params: spawn_cooldown - cooldown para spawnar
            return: None
        """

        if self.__cooldown(spawn_cooldown):
            hunter = self.objeto(self.x, self.y, target)
            hunter.target = target
            self.lista.append(hunter) # add object to list

    def random_spawn_y(self, spawn_cooldown=3) -> None:
        """
        Spawnar o objeto a cada x segundos em um lugar aleatório no y com x do spawner.
            params: spawn_cooldown - cooldown para spawnar
            return: None
        """

        if self.__cooldown(spawn_cooldown):
            self.lista.append(self.__random_create_object(self.objeto)) # add object to list


    def __create_object(self, object):
        return object(self.x, self.y)


    def __random_create_object(self, object):
        return object(self.x, randrange(0, self.y))


    def __cooldown(self, spawn_cooldown=3):
        now = time.get_ticks()

        if now - self.last_tick >= spawn_cooldown*1000:
            self.last_tick = now
            return True
        else:
            return False
