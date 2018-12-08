# turtle is used to dray the board
import turtle
# these are global veriables used throughout the program
TypeList = ["Nothing","Wire","Battery","Resistor","Lightbulb","Switch"]
CompNum = None
point1 = None
point2 = None
comp_1 = None
 
comp_2 = None
 
comp_3 = None
 
comp_4 = None

comp_5 = None

continuity = None

complist = [comp_1, comp_2, comp_3, comp_4, comp_5]

#===============================================================================================================================================
# each component is a subclass of the component class
class component:
    def __init__(self, voltage = 0, resistance = 0, power = 0):
        self.voltage = voltage
        self.resistance = resistance
        self.power = power
class Wire(component):
    def drawcomp(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.foreward(40)
        
class Battery(component):
    
    def gitvoltage(self):
        voltage = float(input('battery voltage:'))
        return voltage
# each drawcomp function draws the component on the board
    def drawcomp(self, x, y):
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(12)
        turtle.left(90)
        turtle.forward(35)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(4)
        turtle.left(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(35)
        turtle.left(90)
        turtle.forward(12)  
class Resistor(component):
    
    def gitresistance(self):
        resistance = float(input('resister resistance:'))
        return resistance
    def drawcomp(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(135)
        for i in range(0,3):
            turtle.forward(10)
            turtle.left(90)
            turtle.forward(10)
            turtle.right(90)
        turtle.left(45)
        turtle.forward(10)

    

class LightBulb(component):
    def __init__(self, voltage, resistance, power, threshold, lightstatus):
        super().__init__(voltage, resistance, power)
    
    def getthreshold(self):
        threshold = float(input('How much power is required to turn on the light?:'))
        return threshold
    def getlightstatus(self):
        lightstatus = input('is the light on or off?:')
        return lightstatus
    def drawcomp(self, x, y):
        turtle.penup()
        turtle.goto(x, y - 10)
        turtle.pendown()
        if lightstatus == 'off':
            turtle.fillcolor('white')
        elif lightstatus == 'on':
            turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
class Switch(component):
    def __init__(self, voltage, resistance, power, switchstatus):
        super().__init__(voltage, resistance, power)
        
    def getstatus(self):
        switchstatus = input('is the switch on or off?:')
        return switchstatus
    def drawcomp(self, x, y):
        turtle.penup()
        turtle.goto(x - 40, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        if switchstatus == 'off':
            turtle.right(45)
            turtle.forward(20)
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.left(45)
        elif switchstatus == 'on':
            turtle.forward(30)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)        
###################################################################


#################################################################

# this function find the voltage between the nodes of the meter
def metervoltage(point1, point2):
    comps = [comp_1.voltage, comp_2.voltage, comp_3.voltage, comp_4.voltage, comp_5.voltage]
    myrange = list(range(point1 - 1, point2))
    if point1 < point2:
        for comp in comps:
            if comp in myrange:
                metervoltage = sum(comps)
    elif point1 > point2:
        myrange1 = list(range(point1-1, 0, -1))
        myrange2 = list(range(point2, 6))
        for comp in comps:
            if comp in myrange1:
                metervoltage1 = sum(comps)
        for comp in comps:
            if comp in myrange2:
                metervoltage2 = sum(comps)
        metervoltage = metervoltage1 + metervoltage2
    elif point1 == point2:
        metervoltage = 0
    return metervoltage
    
####################################################################
# finds the resistance between the nodes
def meterresistance(point1, point2):
    comps = [comp_1.resistance, comp_2.resistance, comp_3.resistance, comp_4.resistance, comp_5.resistance]
    myrange = list(range(point1 - 1, point2))
    if point1 < point2:
        for comp in comps:
            if comp in myrange:
                meterresistance = sum(comps)
    elif point1 > point2:
        myrange1 = list(range(point1-1, 0, -1))
        myrange2 = list(range(point2, 6))
        for comp in comps:
            if comp in myrange1:
                meterresistance1 = sum(comps)
        for comp in comps:
            if comp in myrange2:
                meterresistance2 = sum(comps)
        meterresistance = meterresistance1 + meterresistance2
    elif point1 == point2:
        meterresistance = 0
    return meterresistance
    
###################################################################

#===============================================================================================================================================
def listcheck(CompType):
    try:
        
        if CompType not in TypeList:
            return input("\nTHIS IS NOT A VALID ITEM!\n Please Enter a Valid Item: ").title()
    except Exception as e:
        print (e)
    

def PrintType(CompNum,CompType):
    print(f"\n>> You have inserted a {CompType.upper()} into Slot #{CompNum}.")

def GiveType():
    global comp_1 

    global comp_2 

    global comp_3 

    global comp_4 
    global CompNum
    global comp_5 
    global continuity
    
    CompType = input(f'''\n>> What would you like the type of component #{CompNum} to be?
    \n>> Your options are:
    1: Nothing
    2: Wire
    3: Battery 
    4: Resistor
    5: Lightbulb
    6: Switch
    \n>> Enter Here: ''').title()
    print(f"\n>> You Picked {CompType}.")

    listcheck(CompType)
    
    
    print(TypeList)
    if 5 != 1:
        
        listcheck(CompType)   
        if CompNum == 1:
               
    
            print("  $$  object in list.")
          
            if CompType == TypeList[0]:
                
                PrintType(CompNum,CompType)

            elif CompType == TypeList[1]:
                comp_1 = Wire()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[2]:
                comp_1 = Battery(0, 0, 0)
                comp_1.voltage = comp_1.gitvoltage()
                PrintType(CompNum,CompType)
                

            elif CompType == TypeList[3]:
                comp_1 = Resistor(0, 0, 0)                    
                comp_1.resistance = comp_1.gitresistance()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[4]:
                comp_1 = LightBulb(0, 0, 0, 0, 'off')
                comp_1.lightstatus = comp_1.getlightstatus()
                comp_1.threshold = comp_1.getthreshold()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[5]:
                comp_1 = Switch(0, 0, 0, 'off')
                comp_1.switchstatus = comp_1.getstatus()
                PrintType(CompNum,CompType)

        if CompNum == 2:
            listcheck(CompType)

            
            if CompType == TypeList[0]:
                PrintType(CompNum,CompType)

            elif CompType == TypeList[1]:
                comp_2 = Wire()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[2]:
                comp_2 = Battery(0, 0, 0)
                comp_2.voltage = comp_2.gitvoltage()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[3]:
                comp_2 = Resistor(0, 0, 0)
                comp_2.resistance = comp_2.gitresistance()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[4]:
                comp_2 = LightBulb(0, 0, 0, 0, 'off')
                comp_2.lightstatus = comp_2.getlightstatus()
                comp_2.threshold = comp_2.getthreshold()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[5]:
                comp_2 = Switch(0, 0, 0, 'off')
                comp_2.switchstatus = comp_2.getstatus()
                PrintType(CompNum,CompType)

        if CompNum == 3:
            listcheck(CompType)

           
            if CompType == TypeList[0]:
                    
                PrintType(CompNum,CompType)

            elif CompType == TypeList[1]:
                comp_3 = Wire()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[2]:
                comp_3 = Battery(0, 0, 0)
                comp_3.voltage = comp_3.gitvoltage()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[3]:
                comp_3 = Resistor(0, 0, 0)
                comp_3.resistance = comp_3.gitresistance()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[4]:
                comp_3 = LightBulb(0, 0, 0, 0, 'off')
                comp_3.lightstatus = comp_3.getlightstatus()
                comp_3.threshold = comp_3.getthreshold()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[5]:
                comp_3 = Switch(0, 0, 0, 'off')
                comp_3.switchstatus = comp_3.getstatus()
                PrintType(CompNum,CompType)

        if CompNum == 4:
            listcheck(CompType)

           
            if CompType == TypeList[0]:
                
                PrintType(CompNum,CompType)

            elif CompType == TypeList[1]:
                comp_4 = Wire()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[2]:
                comp_4 = Battery(0, 0, 0)
                comp_4.voltage = comp_4.gitvoltage()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[3]:
                comp_4 = Resistor(0, 0, 0)
                comp_4.resistance = comp_4.gitresistance()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[4]:
                comp_4 = LightBulb(0, 0, 0, 0, 'off')
                comp_4.lightstatus = comp_4.getlightstatus()
                comp_4.threshold = comp_4.getthreshold()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[5]:
                comp_4 = Switch(0, 0, 0, 'off')
                comp_4.switchstatus = comp_4.getstatus()
                PrintType(CompNum,CompType)

        if CompNum == 5:
            listcheck(CompType)

            
            if CompType == TypeList[0]:
                
                PrintType(CompNum,CompType)

            elif CompType == TypeList[1]:
                comp_5 = Wire()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[2]:
                comp_5 = Battery(0, 0, 0)
                comp_5.voltage = comp_5.gitvoltage()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[3]:
                comp_5 = Resistor(0, 0, 0)
                comp_5.resistance = comp_5.gitresistance()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[4]:
                comp_5 = LightBulb(0, 0, 0, 0, 'off')
                comp_5.lightstatus = comp_5.getlightstatus()
                comp_5.threshold = comp_5.getthreshold()
                PrintType(CompNum,CompType)

            elif CompType == TypeList[5]:
                comp_5 = Switch(0, 0, 0, 'off')
                comp_5.switchstatus = comp_5.getstatus()
                PrintType(CompNum,CompType)
        if CompType == TypeList[0]:
            continuity = 1
        complist.append(comp_1)
        complist.append(comp_2)
        complist.append(comp_3)
        complist.append(comp_4)
        complist.append(comp_5)
    return 


#================================================================================================================================================


#===================================================

#===================================================================================================================================================

def Start():
    global CompNum
    
    for num in range(5):

        CompNum = num + 1
    
        if CompNum == 1:
            GiveType()
        

        elif CompNum == 2:
            GiveType()

        elif CompNum == 3:
            GiveType()

        elif CompNum == 4:
            GiveType()

        elif CompNum == 5:
            GiveType()
    return CompNum

#################################################################### 

# this draws the board with out any components
def draw():
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    for i in range(0, 5):
        turtle.forward(60)
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(320)
    turtle.exitonclick()



#####################################################################
def main():
    draw()
    Start()
    print(comp_1.voltage)
    global point1
    global point2
    point1 = int(input('where do you want to place the first node? comp#:'))
    point2 = int(input('second node? comp#:'))
    if continuity == 1:
        print('0-Volts, 0-Amps, 0-Ohms, 0-Watts')
    else:
        volts = metervoltage(point1, point2)
        ohms = meterresistance(point1, point2)
        amps = volts / ohms
        watts = volts * amps
        print(f'{volts}-Volts, {amps}-Amps, {ohms}-Ohms, {watts}-Watts')


    comp_1.drawcomp(190.00,50.00)
    comp_2.drawcomp(90.00,50.00)
    comp_3.drawcomp(-10.00,50.00)
    comp_4.drawcomp(-110.00,50.00)
    comp_5.drawcomp(-210.00,50.00)
    


if __name__ == '__main__':
    main()