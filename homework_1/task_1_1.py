import random

class Animal:
    def __init__(self, name=None, sound=None):
        self.name = name
        self.sound = sound

    def makesound(self):
        pass


class Cat(Animal):
    __random_sounds = ['meow meow mrr...', 'purr...', 'hiss', 'caterwaul']

    def __init__(self, name='Cat', sound='random', color='black'):
        super().__init__(name, sound)
        self.color = color

    def makesound(self, real_sound='same'):
        if real_sound == 'same':
            real_sound = self.sound
        if real_sound == 'random':
            real_sound = random.choice(Cat.__random_sounds)
        print(f'Cat makes a "{real_sound}" sound')


class Dog(Animal):
    __random_sounds = [*['bark bark']*3, 'howl', 'growl', 'whine']

    def __init__(self, name='Dog', sound='random', color='sable'):
        super().__init__(name, sound)
        self.color = color

    def makesound(self, real_sound='same'):
        if real_sound == 'same':
            real_sound = self.sound
        if real_sound == 'random':
            real_sound = random.choice(Dog.__random_sounds)
        print(f'Dog makes a "{real_sound}" sound')


# Examples
c = Cat(sound='sleep...')
c.makesound()

random.seed(1)
c = Cat(color='ginger')
c.makesound() # real_sound == self.sound == 'random'
print(f'Cat is {c.color} colored')
print()

d = Dog(name='Rocky', sound='random')
d.makesound()
print(f'Dog "{d.name}" is {d.color} colored')
