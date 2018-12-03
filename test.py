import turtle

TypeList = ["Nothing","Wire","Battery","Resistor","Lightbulb","Switch"]


global comp_1 
comp_1 = None
global comp_2 
comp_2 = None
global comp_3 
comp_3 = None
global comp_4 
comp_4 = None
global comp_5 
comp_5 = None

global inlist
inlist = None

complist = [comp_1, comp_2, comp_3, comp_4, comp_5]

#===============================================================================================================================================

class component:
    def __init__(self, voltage, resistance, power):
        self.voltage = voltage
        self.resistance = resistance
        self.power = power
class Wire(component):
    def __init__(self, voltage, resistance, power):
        component.__init__(self, voltage, resistance, power)
        self.voltage = 0
        resistance = 0
        power = 0
class Battery(component):
    def __init__(self, voltage, resistance, power):
        component.__init__(self, voltage, resistance, power)
        voltage = 0
        resistance = 0
        power = 0
    def gitvoltage(self):
        voltage = float(input('battery voltage:'))
        return voltage
class Resistor(component):
    def __init__(self, voltage, resistance, power):
        component.__init__(self, voltage, resistance, power)
        voltage = 0
        resistance = 0
        power = 0
    def gitresistance(self):
        resistance = float(input('resister resistance:'))
        return resistance
class LightBulb(component):
    def __init__(self, voltage, resistance, power):
        component.__init__(self, voltage, resistance, power)
        voltage = 0
        resistance = 0
        power = 0
    def getthreshold(self):
        threshold = float(input('How much power is required to turn on the light?:'))
        return threshold
    def getlightstatus(self):
        lightstatus = input('is the light on or off?:')
        return lightstatus
class Switch(component):
    def __init__(self, voltage, resistance, power):
        component.__init__(self, voltage, resistance, power)
        voltage = 0
        resistance = 0
        power = 0
    def getstatus(self):
        switchstatus = input('is the switch on or off?:')
        return switchstatus

###################################################################


#################################################################

def metervoltage(point1, point2, complist):
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

def meterresistance(point1, point2, complist):
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

#===============================================================================================================================================
def listcheck(CompType):
    try:
        if CompType in TypeList:
            inlist = True
        
        if CompType not in TypeList:
            inlist = False
        
        while inlist == False:
            return input("\nTHIS IS NOT A VALID ITEM!\n Please Enter a Valid Item: ").title()
    except Exception as e:
        print (e)


def PrintType(CompNum,CompType):
    print(f"\n>> You have inserted a {CompType.upper()} into Slot #{CompNum}.")

def GiveType(CompNum,comp_1,comp_2,comp_3,comp_4,comp_5):
    continuity = 1
    CompType = input(f'''\n>> What would you like the type of component #{CompNum} to be?
    \n>> Your options are:
    1: Nothing
    2: Wire
    3: Battery (You can only have one battery)
    4: Resistor
    5: Lightbulb
    6: Switch
    \n>> Enter Here: ''').title()
    print(f"\n>> You Picked {CompType}.")

    listcheck(CompType)
    
    if inlist == True:
        print(TypeList)
        if CompNum == 1:
            listcheck(CompType)   
            if inlist == True:
                
                print("  $$  object in list.")
          
                if CompType == TypeList[0]:
                    continuity is False
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_1 = Wire(0, 0, 0)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_1 = Battery(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_1.voltage = comp_1.gitvoltage()

                elif CompType == TypeList[3]:
                    comp_1 = Resistor(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_1.resistance = comp_1.gitresistance()

                elif CompType == TypeList[4]:
                    comp_1 = LightBulb(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_1.lightstatus = comp_1.getlightstatus()
                    comp_1.threshold = comp_1.getthreshold()

                elif CompType == TypeList[5]:
                    comp_1 = Switch(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_1.status = comp_1.getstatus()

        if CompNum == 2:
            listcheck(CompType)

            if inlist == True:
                if CompType == TypeList[0]:
                    continuity is False
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_2 = Wire(0, 0, 0)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_2 = Battery(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_2.voltage = comp_2.gitvoltage()

                elif CompType == TypeList[3]:
                    comp_2 = Resistor(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_2.resistance = comp_2.gitresistance()

                elif CompType == TypeList[4]:
                    comp_2 = LightBulb(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_2.lightstatus = comp_2.getlightstatus()
                    comp_2.threshold = comp_2.getthreshold()

                elif CompType == TypeList[5]:
                    comp_2 = Switch(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_2.status = comp_2.getstatus()

        if CompNum == 3:
            listcheck(CompType)

            if inlist == True:
                if CompType == TypeList[0]:
                    continuity is False
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_3 = Wire(0, 0, 0)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_3 = Battery(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_3.voltage = comp_3.gitvoltage()

                elif CompType == TypeList[3]:
                    comp_3 = Resistor(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_3.resistance = comp_3.gitresistance()

                elif CompType == TypeList[4]:
                    comp_3 = LightBulb(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_3.lightstatus = comp_3.getlightstatus()
                    comp_3.threshold = comp_3.getthreshold()

                elif CompType == TypeList[5]:
                    comp_3 = Switch(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_3.status = comp_3.getstatus()

        if CompNum == 4:
            listcheck(CompType)

            if inlist == True:
                if CompType == TypeList[0]:
                    continuity is False
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_4 = Wire(0, 0, 0)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_4 = Battery(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_4.voltage = comp_4.gitvoltage()

                elif CompType == TypeList[3]:
                    comp_4 = Resistor(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_4.resistance = comp_4.gitresistance()

                elif CompType == TypeList[4]:
                    comp_4 = LightBulb(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_4.lightstatus = comp_4.getlightstatus()
                    comp_4.threshold = comp_4.getthreshold()

                elif CompType == TypeList[5]:
                    comp_4 = Switch(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_4.status = comp_4.getstatus()

        if CompNum == 5:
            listcheck(CompType)

            if inlist == True:
                if CompType == TypeList[0]:
                    continuity is False
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_5 = Wire(0, 0, 0)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_5 = Battery(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_5.voltage = comp_5.gitvoltage()

                elif CompType == TypeList[3]:
                    comp_5 = Resistor(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_5.resistance = comp_5.gitresistance()

                elif CompType == TypeList[4]:
                    comp_5 = LightBulb(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_5.lightstatus = comp_5.getlightstatus()
                    comp_5.threshold = comp_5.getthreshold()

                elif CompType == TypeList[5]:
                    comp_5 = Switch(0, 0, 0)
                    PrintType(CompNum,CompType)
                    comp_5.status = comp_5.getstatus()
        

    return continuity    


#================================================================================================================================================


#===================================================

#===================================================================================================================================================

def Start():
    continuity = 1
    for num in range(5):

        CompNum = num + 1

        if CompNum == 1:
            GiveType(CompNum,comp_1,comp_2,comp_3,comp_4,comp_5)

        if CompNum == 2:
            GiveType(CompNum,comp_1,comp_2,comp_3,comp_4,comp_5)

        if CompNum == 3:
            GiveType(CompNum,comp_1,comp_2,comp_3,comp_4,comp_5)

        if CompNum == 4:
            GiveType(CompNum,comp_1,comp_2,comp_3,comp_4,comp_5)

        if CompNum == 5:
            GiveType(CompNum,comp_1,comp_2,comp_3,comp_4,comp_5)
    return continuity

#################################################################### 


def draw():
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    for i in range(1, 5):
        turtle.forward(70)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(300)

    turtle.exitonclick()

#####################################################################
def main():
    Start()
    point1 = int(input('where do you want to place the first node? comp#:'))
    point2 = int(input('second node? comp#:'))
    volts = metervoltage(point1, point2, complist)
    ohms = meterresistance(point1, point2, complist)
    amps = volts / ohms
    watts = volts * amps
    draw()
    print(f'{volts}-Volts, {amps}-Amps, {ohms}-Ohms, {watts}-Watts')

if __name__ == '__main__':
    main()