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
        print(f"{self.name} มี SpecsComputer ดังนี้ \nCPU : {self.cpu} \nGPU : {self.gpu} \nMB  : {self.mb} \nSSD : {self.ssd}GB \nPSU : {self.psu} \nRAM : {self.ram}GB")

class Game(Computer):
    def re4(self):
        print(self.ram)

obj1 = Game("แดง","Intel i3-10105f","GTX1050","Auros B356",250,'550W',16)
obj1._reportSpecs()
obj1.re4()