class MPU9250:
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address