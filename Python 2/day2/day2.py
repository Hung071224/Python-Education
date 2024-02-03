








class Dragonball():
    def __init__(self, name, level, hair, power):
        self.name = name
        self.level = level
        self.hair = hair
        self.power = power
        
    def level_up(self):
        self.level += 1
        self.power += 1000
        print(f"{self.name} đã tăng lên level {self.level} và có power là {self.power}")
    
    def reset(self):
        self.level = 1
        self.power = 10
        print(f"{self.name} đã trở lại level ban đầu và có power là {self.power}")
        
    def super_saiyan(self, number, hairs_color):
        self.level += (10 * number)
        self.hair = hairs_color
        self.power *= number
        print(f"{self.name} đã biến thành super saiyan {number} với màu tóc  là {self.hair} và có level là {self.level}")
    
    def show(self):
        print(f"Thông tin của nhân vật {self.name}: ")
        print(f"Level: {self.level} ")
        print(f"Hair: {self.hair} ")
        print(f"Powers: {self.power} ")
                      
goku = Dragonball("Goku", 1, "black", 10)        
vegeta = Dragonball("vegeta", 2, "black", 20)  
gohan = Dragonball("gohan", 3, "black", 30)

goku.level_up()
vegeta.super_saiyan(2, "yellow")
gohan.show()


















































