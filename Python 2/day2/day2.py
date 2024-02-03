







class DragonBall:
    def __init__(self, name, level, hair, power):
        self.name = name
        self.level = level
        self.hair = hair
        self.power = power
        
    def level_up(self):
        self.level += 1
        self.power += 1000
        print(f"Level Up!!!!!")
    
    def reset(self):
        self.level = 1
        self.power = 10
        self.hair = "black"
        print(f"Reset!!!")
        
    def super_saiyan(self, number, hair_color):
        self.level += (number * 10)
        self.hair = hair_color
        self.power *= number
        print(f"SUPER SAIYAN!!!!!")
    
    def show(self):
        print(f"Name: {self.name} ,Level: {self.level},Hair: {self.hair},Powers: {self.power}")

                      



chap1 = DragonBall("Goku", 1, "black", 1000)
chap1.show()
chap1.level_up()
chap1.show()















































