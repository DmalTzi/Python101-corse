class Computer:
    
    def __init__(self,name,cpu,gpu,mb,ssd,psu,ram):
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.mb  = mb
        self.ssd = ssd
        self.psu = psu
        self.ram = ram

    def _reportSpecs(self):
        print("=====================")
        print(f"{self.name} มี SpecsComputer ดังนี้ \nCPU : {self.cpu} \nGPU : {self.gpu} \nMB  : {self.mb} \nSSD : {self.ssd}GB \nPSU : {self.psu} \nRAM : {self.ram}GB")
        print("=====================")

class Game(Computer):
    def _re4remake(self):
        print(f"คอมสเปคนี้สามารถเล่น RE4remake ได้ไหม")
        print("เล่นได้") if self.ram >= 8 else print("ไม่สามารถเล่นได้")
        print("-------------------")

    def _stardew(self):
        print("คอมสเปคนี้สามารถเล่น Stardew valley ได้ไหม")
        print("เล่นได้") if self.ram >= 8 else print("ไม่สามารถเล่นได้")
        print("-------------------")

    def _ow2(self):
        print("คอมสเปคนี้สามารถเล่น Overwatch2 ได้ไหม")
        print("เล่นได้") if self.ram >= 8 else print("ไม่สามารถเล่นได้")
        print("-------------------")

obj1 = Game("แดง","Intel i3-10105f","GTX1050","Auros B356",250,'550W',16)
obj1._reportSpecs()
obj1._re4remake()
obj1._ow2()

obj2 = Game("เขียว", "AMD Ryzen 5 5600", "Radeon rx 570","Auros B550",500,'550W',32)
obj2._reportSpecs()
obj2._ow2()
obj2._stardew()