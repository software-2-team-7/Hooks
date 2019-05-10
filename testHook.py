class run:

    packet = ""

    def __init__(self, packet):
        self.packet = packet
        print("Initialized.")

    def execute(self):
        packet = self.packet
        print("Running!")
        return ("Function run!"  + self.packet + " ")




