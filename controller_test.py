import pygame
import threading
import queue
import time
import serial

# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')
colors = (RED,GREEN,BLUE)

# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

# convert <3 digit ints to 3 digit string
def three_digit_str(num):
    three_str = ''
    if (num > 99):
        three_str = str(num)
    elif (num < 10):
        three_str = "0" + "0" + str(num)
    elif (num < 100):
        three_str = "0" + str(num)
    return three_str

pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

# Game Definitions
try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except serial.SerialException or OSError:
    print("Couldn't open tower port")
    quit()
flag = 1
location = '000'
number = 0
updt_loc = False
color_index = 0
updt_color = False
player = 0
prev_player = 0
move = False
reset = True

# -------- Main Program Loop -----------
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        textPrint.tprint(screen, "Joystick {}".format(i))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        textPrint.tprint(screen, "Joystick name: {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        textPrint.unindent()

        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen,
                             "Button {:>2} value: {}".format(i, button))
        textPrint.unindent()

        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()

        textPrint.unindent()

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #
        updated_loc = updt_loc
        if updt_loc:
            location = three_digit_str(number)
            updt_loc = False

        updated_color = updt_color
        if updt_color is True:
            color_index = (color_index+1)%3
            print('index: ', color_index)
            updt_color = False
            
        if move:
            if player < 100:
                prev_player = player
                player += 1
            move = False
        
        test = joystick.get_axis(0)
        if (test > 0.5):
            updt_loc = True
            number = (number + 4)%96
        elif( test <-0.5):
            updt_loc = True
            number = (number - 4)%96
            
        if(joystick.get_button(0) == 1):
            updt_color = True
        
        if(joystick.get_button(1) == 1):
            move = True
            
        if(joystick.get_button(4) == 1):
            reset = True
            
        if ( flag == 1):
            time.sleep(10)
            print("Done")
            flag = 0
            
        if updated_loc:
            #print(location)
            message = 'GoTo' + location + '\n'
            print(message)
            ser.write(message.encode())
            
        
        if updated_color:
            r = three_digit_str(colors[color_index].r)
            g = three_digit_str(colors[color_index].g)
            b = three_digit_str(colors[color_index].b)
            message = 'L' + three_digit_str(5) + ',' + r + ',' + g + ',' + b + '\n'
            print(message)
            ser.write(message.encode())
        
        if prev_player != player:
            message_off = 'M' + three_digit_str(prev_player) + ',000,000,000\n'
            message_on = 'M' + three_digit_str(player) + ',050,050,050\n'
            print(message_off)
            print(message_on)
            ser.write(message_off.encode())
            time.sleep(0.16)
            ser.write(message_on.encode())
            prev_player = player
            
        if reset:
            all_off = 'AllOff\n'
            print(all_off)
            ser.write(all_off.encode())
            
            prev_player = 0
            player = 0
            message_on = 'M' + three_digit_str(player) + ',255,255,255\n'
            ser.write(message_on.encode())

            message = 'GoTo' + '000' + '\n'
            print(message)
            ser.write(message.encode())
            
            color_index = 0
            
            reset = False
        
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()