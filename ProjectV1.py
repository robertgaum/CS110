def PrintOptions():
    print(">> Your options are: \n 1: Nothing \n 2: Wire\n 3: Battery (You can only have one battery)\n 4: Resistor\n 5: Lightbulb \n 6: Switch")

#================================================================================================================================================

class Component:
    def __init__(self, CompType = None):
        self.Type = CompType

    def Build(CompNum):
        pass    
        

# class Nothing(Component):
#     def __init__(self, Comptype, voltage, current, Ohm):
#         super().__init__(CompType)
#         self.voltage = 0
#         self.current = 0
#         self.Ohm = 0

class Wire(Component):
    def __init__(self, Type, voltage, Ohm):
        super().__init__(Type)
        

class Battery(Component):
    def __init__(self, TotalVoltage = None):
        self.voltage = TotalVoltage
    
    def DefBatVoltage():
        TotalVoltage = input("\n>> Enter Voltage for battery: ")

class Resistor(Component):
    pass

class LightBulb(Component):
    pass

class Switch(Component):
    pass

#===================================================================================================================================================

def Start():
    for num in range(5):
        PrintOptions()
        if num == 1:
            pass 

        if num == 2:
            pass

        if num == 3:
            pass

        if num == 4:
            pass

        if num == 5:
            pass

def main():
    Start()

if __name__ == '__main__':
    main()

