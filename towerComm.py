import serial
class towerComm:

    def __init__(self):
        ser = serial.Serial('/dev/ttyACM0', 115200)
        return

    # send anything you want
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

    # send the stop command
    def stop(self):
       self.ser.write("Stop\n".encode())
       return

    # tell tower to go to a position between 0 and 96
    def GoTo(self, position):
        message = "GoTo"
        if(position > 96):
            position -= 96
        if (position < 0):
            position += 96
        if(position < 10):
            message += "00" + position
        else:
            message += "0" + position

        message += "\n"
        self.ser.write(message.encode())
        return

    # move the tower clockwise by a certain increment
    def CW(self, incriment):
        message = "JogF"
        if(incriment < 10):
            message += "0" + incriment
        else:
            message += incriment
        message += "\n"
        self.ser.write(message.encode())
        return

    # move the tower counter clockwise by a certain increment
    def CCW(self, incriment):
        message = "JogR"
        if(incriment < 10):
            message += "0" + incriment
        else:
            message += incriment
        message += "\n"
        self.ser.write(message.encode())
        return

    # move the tower clockwise one step
    def forward(self):
        self.ser.write("For\n".encode())
        return

    # move the tower counter clockwise one step
    def forward(self):
        self.ser.write("Rev\n".encode())
        return


