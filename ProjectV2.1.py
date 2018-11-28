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


#===============================================================================================================================================

class Component:
    def __init__(self, CompType = None):
        self.Type = CompType

class Nothing(Component): pass
    # def __init__(self, Comptype, voltage, current, Ohm):
    #     super().__init__(CompType)
    #     self.voltage = 0
    #     self.current = 0
    #     self.Ohm = 0

class Wire(Component): pass
#     def __init__(self, Type, voltage, Ohm):
#         super().__init__(Type)

        

class Battery(Component):
    def __init__(self, TotalVoltage = None):
        self.voltage = TotalVoltage
        self.type = "Battery"
    
    def DefBatVoltage(self, TotalVoltage = None):
        TotalVoltage = input("\n>> Enter Voltage for battery: ")
        print(f"\n>> TOTAL VOLTAGE = {TotalVoltage}")

class Resistor(Component):
    def __init__(self, Resistance = None):
        self.Resistance = Resistance


class LightBulb(Component):
    pass

class Switch(Component):
    pass

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
                    comp_1 = Nothing(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_1 = Wire(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_1 = Battery(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[3]:
                    comp_1 = Resistor(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[4]:
                    comp_1 = LightBulb(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[5]:
                    comp_1 = Switch(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)
        
        if CompNum == 2:   
            if inlist == True:

                if CompType == TypeList[0]:
                    comp_2 = Nothing(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_2 = Wire(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_2 = Battery(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[3]:
                    comp_2 = Resistor(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[4]:
                    comp_2 = LightBulb(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[5]:
                    comp_2 = Switch(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)
        
        if CompNum == 3:   
            if inlist == True:

                if CompType == TypeList[0]:
                    comp_3 = Nothing(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_3 = Wire(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_3 = Battery(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[3]:
                    comp_3 = Resistor(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[4]:
                    comp_3 = LightBulb(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[5]:
                    comp_3 = Switch(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

        if CompNum == 4:   
            if inlist == True:

                if CompType == TypeList[0]:
                    comp_4 = Nothing(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_4 = Wire(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_4 = Battery(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[3]:
                    comp_4 = Resistor(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[4]:
                    comp_4 = LightBulb(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[5]:
                    comp_4 = Switch(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

        if CompNum == 5:   
            if inlist == True:

                if CompType == TypeList[0]:
                    comp_5 = Nothing(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[1]:
                    comp_5 = Wire(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[2]:
                    comp_5 = Battery(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[3]:
                    comp_5 = Resistor(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[4]:
                    comp_5 = LightBulb(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)

                elif CompType == TypeList[5]:
                    comp_5 = Switch(Component)
                    listcheck(CompType)
                    PrintType(CompNum,CompType)
        


#================================================================================================================================================


#===================================================

#===================================================================================================================================================

def Start():
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

def main():
    Start()

if __name__ == '__main__':
    main()

