'''Enemy Factory using abstract method.'''
import abc
class EnemyFactory(abc.ABC):
  @abc.abstractmethod
  def create_random_enemy(self):
    #Enemy
    pass

