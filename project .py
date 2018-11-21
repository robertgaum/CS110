class component:
    def __init__(self, voltage, resistance, current, power):
        self.voltage = voltage
        self.resistance = resistance
        self.current = current
        self.power = power
class wire(component):
    def __init__(self, voltage, resistance, current, power):
        super().__init__()
        self.voltage = 0
        self.resistance = 0
        self.current = 0
        self.power = 0
class battery(component):
    def __init__(self):
        super().__init__()
    def gitvoltage(self):
        voltage = float(input('battery voltage:'))
        return voltage
class resister(component):
    def __init__(self):
        super().__init__()
    def gitresistance(self):
        resistance = float(input('resister resistance:'))
        return resistance
