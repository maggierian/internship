class Car():

def __init__ (self,name,manufacturer,fuel):
    self.name= name
    self.manufacturer=manufacturer
    self.health= 10
    self.fuel=''
    self.History=[]

def knock(self, Knocked_car)
    Knocked_car.health =Knocked_car.health-1
    self.recordHistory ('{} has knocked {}'.format(self.name, Knocked_car.name))
    Knocked_car.recordHistory ('{} has been knocked by {} and My new health dropped to {}'.format(Knocked_car.name, self.name, knocked_car.health) )



def recordHistory(self, message):
     self.history.append(message)
    
def showHistory(self):
     print(self.history)


buggati = Car('Buggati', 'China', 5)
royce = Car('Royce', 'Japan', 3)
raum = Car('Raum', 'England', 0)
platz = Car('Platz', 'Germany', 4)
rover = Car('Rover', 'Chile', 0)

buggati.knock(royce)

buggati.showHistory()