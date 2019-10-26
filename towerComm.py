import serial
class towerComm:

    def __init__(self):
        ser = serial.Serial('/dev/ttyACM0', 115200)
        return

    def sendAnything(self, message):
        message += "\n"
        self.ser.write(message.encode())

    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def lowerBandLight(self, position, color):
        string = "Lx"
        if(position < 10):
            string += "00"+position
        elif (position < 100):
            string += "0" + position
        elif (position > 100):
            string += position

        for i in range(0, 2):
            if (color[i] < 10):
                string += "00" + color[i]
            elif (color[i] < 100):
                string += "0" + color[i]
            elif (color[i] > 100):
                string += color[i]

        string += "\n"
        self.ser.write(string.encode())
        return

    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def middleBandLight(self, position, color):
        string = "Mx"
        if(position < 10):
            string += "00"+position
        elif (position < 100):
            string += "0" + position
        elif (position > 100):
            string += position

        for i in range(0, 2):
            if (color[i] < 10):
                string += "00" + color[i]
            elif (color[i] < 100):
                string += "0" + color[i]
            elif (color[i] > 100):
                string += color[i]

        string += "\n"
        self.ser.write(string.encode())
        return

    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def upperBandLight(self, position, color):
        string = "Hx"
        if(position < 10):
            string += "00"+position
        elif (position < 100):
            string += "0" + position
        elif (position > 100):
            string += position

        for i in range(0, 2):
            if (color[i] < 10):
                string += "00" + color[i]
            elif (color[i] < 100):
                string += "0" + color[i]
            elif (color[i] > 100):
                string += color[i]

        string += "\n"
        self.ser.write(string.encode())
        return



