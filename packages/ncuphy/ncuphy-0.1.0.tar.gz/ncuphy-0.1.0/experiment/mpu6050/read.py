class MPU6050:
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address