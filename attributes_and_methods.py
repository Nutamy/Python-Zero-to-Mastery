class PlayCharacter:
  # Class Object AttributeError
  membership = True
  def __init__(self, name, age):
    if(PlayCharacter.membership):
      self.name = name
      self.age = age

  def shout(self):
    print(f'My name is {self.name}')

player1 = PlayCharacter('Cindy', 45)
player2 = PlayCharacter('Tim', 18)

print(player1.shout())
print(player2.shout())
