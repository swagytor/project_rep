class Hero:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
        self.armor = 50
        self.all_hp = self.hp + self.armor


hero = Hero(100, 5)

print(hero.hp)
print(hero.armor)
print(hero.all_hp)
