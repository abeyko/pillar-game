import serial
import time
class towerComm:
    #PORT = '/dev/ttyACM0'
    PORT = 'COM5'
    def __init__(self):
        self.ser = serial.Serial(self.PORT, 115200)
        time.sleep(6)
        self.sendAnything("Home")

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

    def two_digit_str(self, num):
        two_str = ''
        if (num < 10):
            three_str = "00" + str(num)
        elif (num < 100):
            three_str = "0" + str(num)
        return two_str
    
    # output format "ppp,rrr,ggg,bbb"
    def pos_color_str(self, position, color):
        pos = self.three_digit_str(position)
        r = self.three_digit_str(color[0])
        g = self.three_digit_str(color[1])
        b = self.three_digit_str(color[2])
        num_str = pos + ',' + r + ',' + g + ',' + b
        return num_str
    
    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def lowerBandLight(self, position, color):
        string = "L"
        string += self.pos_color_str(position, color)
        string += "\n"
        self.ser.write(string.encode())
        print(string)
        return

    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def middleBandLight(self, position, color):
        string = "M"
        string += self.pos_color_str(position, color)
        string += "\n"
        self.ser.write(string.encode())
        print(string)
        return

    # tells the tower to light up a certain led with a certain color in the lower band
    # the color variable is a tuple like this: (r, g, b)
    def upperBandLight(self, position, color):
        string = "H"
        string += self.pos_color_str(position, color)
        string += "\n"
        self.ser.write(string.encode())
        print(string)
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
        elif (position < 0):
            position += 96
        if(position < 10):
            message += "00" + str(position)
        else:
            message += "0" + str(position)

        message += "\n"
        self.ser.write(message.encode())
        return

    # move the tower clockwise by a certain increment
    def CW(self, incriment):
        message = "JogF"
        if(incriment < 10):
            message += "0" + str(incriment)
        else:
            message += str(incriment)
        message += "\n"
        self.ser.write(message.encode())
        return

    # move the tower counter clockwise by a certain increment
    def CCW(self, incriment):
        message = "JogR"
        if(incriment < 10):
            message += "0" + str(incriment)
        else:
            message += str(incriment)
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


