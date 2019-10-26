import serial
class towerComm:

    def __init__(self):
        ser = serial.Serial('/dev/ttyACM0', 115200)
        return

    # send anything you want
    def sendAnything(self, message):
        message += "\n"
        self.ser.write(message.encode())

    # convert <3 digit ints to 3 digit string
    def three_digit_str(self, num):
        three_str = ''
        if (num > 99):
            three_str = str(num)
        elif (num < 10):
            three_str = "00" + str(num)
        elif (num < 100):
            three_str = "0" + str(num)
        return three_str

    # output format "ppp,rrr,ggg,bbb"
    def pos_color_str(self, position, color):
        pos = three_digit_str(position)
        r = three_digit_str(color.r)
        g = three_digit_str(color.g)
        b = three_digit_str(color.b)
        num_str = pos + ',' + r + ',' + g + ',' + b
        return color
    
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
        return# tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def lowerBandLight(self, position, color):
        string = "Lx"
        string += pos_color_str(self, position, color)
        string += "\n"
        self.ser.write(string.encode())
        return

    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def middleBandLight(self, position, color):
        string = "Mx"
        string += pos_color_str(self, position, color)
        string += "\n"
        self.ser.write(string.encode())
        return

    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def upperBandLight(self, position, color):
        string = "Hx"
        string += pos_color_str(self, position, color)
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
    def reverse(self):
        self.ser.write("Rev\n".encode())
        return


