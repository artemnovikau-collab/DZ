class Main_Character:
    def __init__ (self, name, maxhp, skills, maxmana,speed):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.skills = skills
        self.maxmana = maxmana
        self.mana = maxmana
        self.speed = speed
    def status(self):
        print(f"\n" + "=" * 15 + "СТАТУС ГЛАВНОГО ПЕРСОНАЖА" + "=" * 15 + "\n")
        print(self.name)
        print(f"{self.hp}/{self.maxhp} HP")
        print(f"{self.mana}/{self.maxmana} Mana")
        print(f"Длина шага: {self.speed}")

        print("Скиллы:")
        for i in range(len(self.skills)):
            self.skills[i].status()
    def UseSkill(self,skill,target):
        if skill in self.skills:
            target.hp -= skill.damage
            self.mana -= skill.mana
        print(f"{self.name} использует {skill.name} на {target.name}")
        self.status()
        target.status()
    def Step(self,count):
        print(f"{self.name} проходит {count} шагов({count*self.speed} метров)")
    def Jump(self):
        print(self.name,"прыгает")

class Platform:
    def __init__(self,color,xChange,yChange,velocity):
        self.color = color
        self.xChange = xChange
        self.yChange = yChange
        self.velocity = velocity
    def status(self):
        print(f"\n"+"="*15+"СТАТУС ПЛАТФОРМЫ"+"="*15+"\n")
        print(f"Цвет: {self.color}")
        print(f"Платформа движется на {self.xChange} по горизонтали и {self.yChange} по вертикали со скоростью {self.velocity}")

class Skill:
    def __init__(self,name,damage,range,mana,special=""):
        self.name = name
        self.range = range
        self.damage = damage
        self.mana = mana
        self.special = special
    def status(self):

        print(f"   {self.name}: \n      {self.damage} урона \n      {self.range} радиус атаки \n      {self.mana} маны для каста")
        if self.special !="":
            print("      "+self.special)
class Basic_Enemy():
    def __init__(self,name,maxhp,damage,attackspeed,speed):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.damage = damage
        self.ATKspeed = attackspeed
        self.speed = speed

    def status(self):
        print(f"\n" + "=" * 15 + "СТАТУС ВРАГА" + "=" * 15 + "\n")
        print(self.name)
        print(f"{self.hp}/{self.maxhp} HP")
        print(f"Длина шага: {self.speed}")
        print(f"Время на 1 атаку: {self.ATKspeed}")
    def Step(self,count):
        print(f"{self.name} проходит {count} шагов({count * self.speed} метров)")
    def Attack(self,time, target):
        print(f"{self.name} атакует{target.name} в течении {time}, бьёт {time//self.ATKspeed} раз и наносит {time//self.ATKspeed*self.damage} урона")
        self.status()
        target.status()
class Boss_Enemy():
    def __init__(self,name,maxhp,damage,attackspeed,speed, skills, maxmana):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.damage = damage
        self.ATKspeed = attackspeed
        self.speed = speed
        self.maxmana = maxmana
        self.mana = maxmana
        self.skills = skills

    def status(self):
        print(f"\n" + "=" * 15 + "СТАТУС БОССА" + "=" * 15 + "\n")
        print(self.name)
        print(f"{self.hp}/{self.maxhp} HP")
        print(f"Длина шага: {self.speed}")
        print(f"Время на 1 базовую атаку: {self.ATKspeed}")
        print(f"{self.mana}/{self.maxmana} Mana")
        print("Скиллы:")
        for skill in self.skills:
            skill.status()

    def Step(self,count):
        print(f"{self.name} проходит {count} шагов({count * self.speed} метров)")
    def BasicAttack(self,time, target):
        print(f"{self.name} атакует{target.name} в течении {time}, бьёт {time//self.ATKspeed} раз и наносит {time//self.ATKspeed*self.damage} урона")
        self.status()
        target.status()
    def UseSkill(self,skill,target):
        if skill in self.skills:
            target.hp -= skill.damage
            self.mana -= skill.mana
            print(f"{self.name} использует {skill.name} на {target.name}")
            self.status()
            target.status()

Fireball = Skill("Фаербол",15,5,20)
Burst = Skill("Взрыв 5ой точки",30,10,80)
Savic = Skill("Выкрик: САВИЦЕЛИЙ КАНОН",1,20,0)
Kurs = Skill("Выкрик: КУРС ГОЛУБЬ",1,20,0)
Har = Skill("Харакири",9999999999999,-1,-10)

BloodBlade = Skill("кровавый клинок",25,3,30)
BloodChains = Skill("Кровяная цепь",10,7,25, "Станит на 5 секунд")
BloodHunt = Skill("Кровяная охота",5,15,75,"Уменьшает урон и скорость передвижения на 20% на 20 секунд")

mc = Main_Character("Стас", 100, [Fireball,Burst,Savic,Kurs,Har], 100,2)
pl1 = Platform("Красный", 10, 1, 5)
en = Basic_Enemy("Дьявольский миньон", 20, 5,2,1)
boss = Boss_Enemy("Гига дьявольский миньон", 100, 15,1,2,[BloodBlade,BloodChains,BloodHunt],100)

gameWorld = [pl1, mc, en, boss]
def ShowGameWorld(gameWorld):
    for obj in gameWorld:
        obj.status()
ShowGameWorld(gameWorld)
