# Character is a superclass
class Character:
    def interactWith(self, obstacle): pass

class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a", obstacle.__class__.__name__)

class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a", obstacle.__class__.__name__)


# Obstacle is a superclass
class Obstacle: pass

class Puzzle(Obstacle): pass

class NastyMonster(Obstacle): pass


# AbstractFactory creates objects subclassed from Character and Obstacle
class AbstractFactory:
    def makeCharacter(self): pass
    def makeObstacle(self): pass

class FunFactory(AbstractFactory):
    @staticmethod
    def makeCharacter(): return Kitty()
    @staticmethod
    def makeObstacle(): return Puzzle()

class ViolentFactory(AbstractFactory):
    @staticmethod
    def makeCharacter(): return KungFuGuy()
    @staticmethod
    def makeObstacle(): return NastyMonster()


def play(factory):
    c = factory.makeCharacter()
    ob = factory.makeObstacle()
    c.interactWith(ob)

play(FunFactory)
play(ViolentFactory)