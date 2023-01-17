class Hero:
    
    def __init__(self,name,Health,attackPower):
        self.__name = name
        self.__Health = Health
        self.__attPower = attackPower
       
    
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__Health
    
    
    
    def diserang(self,seranganPower):
        self.__Health -= seranganPower
    
    def setAttPower(self,Nilaibaru):
        self.__attPower = Nilaibaru
    

Jett = Hero("Jett",100 ,10)



print(Jett.getName())
print(Jett.getHealth())
Jett.diserang(10)
print(Jett.getHealth())