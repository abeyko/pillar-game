import threading
import queue
import time
import serial

dwellTime = 0.5
shortTime = 0.01
longTime = 30
        
def main():
    print("Begin.")
    flag = True
    trueCounter = 0
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(longTime)
    
    while(flag):
        if (ser.in_waiting > 0):
            print("YES")
            line = ser.readline()
            new_line = line.decode("utf-8")
            print(new_line)
            isItTrue = new_line.find("Wireless confirmed")
            if (isItTrue != -1):
                trueCounter += 1
                print("I do I do I do ooooo")
                #print(new_line)
            if (trueCounter == 2):
                flag = False
                message1 = "DimWhite\n"
                ser.write(message1.encode())
                time.sleep(longTime)
    print("End.")
    
    flag = True
    trueCounter = 0
    
    while(flag):
        if (ser.in_waiting > 0):
            print("YES")
            line = ser.readline()
            new_line = line.decode("utf-8")
            print(new_line)
            isItTrue = new_line.find("Here")
            if (isItTrue != -1):
                trueCounter += 1
                print("I do I do I do ooooo")
            else:
                "Nu uh"
            if (trueCounter == 1):
                flag = False
                message2 = "AllOff\n"
                ser.write(message2.encode())
                time.sleep(10)
                message3 = "Murica\n"
                ser.write(message3.encode())
                time.sleep(10)
                message4 = "AllBlue\n"
                ser.write(message4.encode())
                time.sleep(10)
                message5 = "AllOff\n"
                ser.write(message5.encode())
                
            else:
                "Nope"
    print("End.")
    

        

if (__name__ == '__main__'):
        main()

    
    
    

