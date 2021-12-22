
class PlayCharacter:
  # Class Object AttributeError
  membership = True
  def __init__(self, name, age):
    if(PlayCharacter.membership):
      self.name = name
      self.age = age

  def shout(self):
    return f'My name is {self.name}'

  def run(self):
    return f'{self.name} runs about {self.age} km'

  def sleep(self):
    print(f'{self.name} is sleeping\n')


player1 = PlayCharacter('Cindy', 45)
player2 = PlayCharacter('Tim', 18)


print(player1.shout())
print(player1.run())
player1.sleep()

print(player2.shout())
print(player2.run())
