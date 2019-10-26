import threading
import queue
import time
import serial

dwellTime = 0.5
shortTime = 0.01
longTime = 30

def read_kbd_input(inputQueue):
    dwellTime = 0.5
    shortTime = 0.01
    longTime = 10
    flag = True
    while(flag):
        print("I'm doing it!")
        input_str = input()
        #inputQueue.put(input_str)
        #time.sleep(longTime)
        #inputQueue.put("Golden")
        #inputQueue.put(input_str)
        #time.sleep(dwellTime)
        #inputQueue.put("All off")
        flag = False
        
        
def main():
    print("hello")
    
    #EXIT_COMMAND = "exit"
    #inputQueue = queue.Queue()
    
    #read_kbd_input(inputQueue)
    
    '''
    if (inputQueue.qsize() > 0):
        print("It is greater than zero")
    else:
        print("It is not greater than zero")
    
    #inputThread = threading.Thread(target=read_kbd_input, args=(inputQueue,), daemon=True)
    #inputThread.start()
    
    #ser = serial.Serial('/dev/ttyACM0', 9600)
    '''
    
    print("Begin.")
    flag = True
    trueCounter = 0
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(longTime)
    
    while(flag):
        if (ser.in_waiting > 0):
            print("YES")
            line = ser.readline()
            print(type(line))
            new_line = line.decode("utf-8")
            print(new_line)
            print(type(new_line))
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
            
        '''time.sleep(dwellTime)
        message1 = "Golden\n"
        ser.write(message1.encode())
        if (ser.in_waiting > 0):
            print("YES")
            line = ser.readline()
            print(line)
        time.sleep(dwellTime)
        message2 = "Murica\n"
        ser.write(message1.encode())
        if (ser.in_waiting > 0):
            print("YES")
            line = ser.readline()
            print(line)
        time.sleep(dwellTime)
        message3 = "All off\n"
        ser.write(message1.encode())
        if (ser.in_waiting > 0):
            print("YES")
            line = ser.readline()
            print(line)'''
        
        '''message0 = "HELOOOO!"
        ser.write(message0.encode())
        message1 = inputQueue.qsize()
        print(message1)
        if(inputQueue.qsize() > 0):
            message = inputQueue.get() + '\n'
            ser.write(message.encode())
            if (message == EXIT_COMMAND):
                print("Exiting serial terminal.")
                break
            
        if (ser.in_waiting > 0):
            line = ser.readline()
            print(line)
        time.sleep(0.01)'''
        #flag = False
    #flag = False
    print("End.")
    
    flag = True
    trueCounter = 0
    
    while(flag):
        if (ser.in_waiting > 0):
            print("YES")
            line = ser.readline()
            print(type(line))
            new_line = line.decode("utf-8")
            print(new_line)
            print(type(new_line))
            isItTrue = new_line.find("Here")
            if (isItTrue != -1):
                trueCounter += 1
                print("I do I do I do ooooo")
            else:
                "Nu uh"
                #print(new_line)
            if (trueCounter == 1):
                flag = False
                message2 = "Murica\n"
                ser.write(message2.encode())
                time.sleep(longTime)
            else:
                "Nope"
        

if (__name__ == '__main__'):
        main()

    
    
    