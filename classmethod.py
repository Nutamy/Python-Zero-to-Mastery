# OOP
class PlayCharacter:
  # Class Object AttributeError
  membership = True
  def __init__(self, name, age):
    self.name = name #attributes
    self.age = age

  def shout(self):
    return f'My name is {self.name}'

  def run(self):
    return f'{self.name} runs about {self.age} km'

  def sleep(self):
    print(f'{self.name} is sleeping\n')

  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Tedy', num1 + num2)

  @staticmethod
  def adding_things2(num1, num2):
    return num1 + num2

player3 = PlayCharacter.adding_things(4,6)

print(player3.age) # 10

# print(PlayCharacter.adding_things(2,1))


# player1 = PlayCharacter('Cindy', 45)
# player2 = PlayCharacter('Tim', 18)

# print(player2.adding_things(9,100))

# print(player1.shout())
# print(player1.run())
# player1.sleep()

# print(player2.shout())
# print(player2.run())
