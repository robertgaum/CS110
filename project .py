class component:
    def __init__(self, voltage, resistance, power):
        self.voltage = voltage
        self.resistance = resistance
        self.power = power
class wire(component):
    super().__init__()
    voltage = 0
    resistance = 0
    power = 0
class battery(component):
    super().__init__()
    voltage = 0
    resistance = 0
    power = 0
    def gitvoltage(self):
        voltage = float(input('battery voltage:'))
        return voltage
class resister(component):
    super().__init__()
    voltage = 0
    resistance = 0
    power = 0
    def gitresistance(self):
        resistance = float(input('resister resistance:'))
        return resistance
class lightbulb(component):
    super().__init__()
    voltage = 0
    resistance = 0
    power = 0
    def getthreshold(self):
        threshold = float(input('How much power is required to turn on the light?:'))
        return threshold
    def getlightstatus(self):
        lightstatus = input('is the light on or off?:')
        return lightstatus
class switch(component):
    super().__init__()
    voltage = 0
    resistance = 0
    power = 0
    def getstatus(self):
        switchstatus = input('is the switch on or off?:')
        return switchstatus

###################################################################

point1 = input('where do you want to place the first node? comp#:')
point2 = input('second node? comp#:')
complist = [comp_1, comp_2, comp_3, comp_4, comp_5]

metercurrent = metervoltage / meterresistance

meterpower = metervoltage * metercurrent

#################################################################

def metervoltage(point1, point2):
    if point1 < point2:
        while point1 <= point2:
            metervoltage = complist[point1 - 1].voltage + complist[point1].voltage
            point1 = point1 + 1
    elif point1 > point2:
        while point1 <= 5:
            metervoltage = complist[point1 - 1].voltage = complist[point1 - 2].voltage
            point1 = point1 - 1
        while point1 <= 5:
            metervoltage = complist[point2 - 1].voltage = complist[point2].voltage
            point2 = point2 + 1
    elif point1 == point2:
        metervoltage = 0
    return metervoltage

####################################################################

def meterresistance(point1, point2):
    if point1 < point2:
        while point1 <= point2:
            meterresistance = complist[point1 - 1].voltage + complist[point1].voltage
            point1 = point1 + 1
    elif point1 > point2:
        while point1 <= 5:
            meterresistance = complist[point1 - 1].voltage = complist[point1 - 2].voltage
            point1 = point1 - 1
        while point1 <= 5:
            meterresistance = complist[point2 - 1].voltage = complist[point2].voltage
            point2 = point2 + 1
    elif point1 == point2:
        meterresistance = 0
    return meterresistance

###################################################################

def draw():