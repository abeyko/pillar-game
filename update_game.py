import towerComm.py
import Character.py

MAX_POS = 300  # num leds in strip
MAX_LOC = 96   # num encoder vals

first_run = True

# pillar vars
loc_str = '000'
cur_loc = 0
updt_loc = False
send_loc = False

# rand led vars
color_index = 0
updt_color = False
send_color = False

# player vars
player = 0
prev_player = 0
updt_pos = False
send_pos = False

reset = True

def update_values(self):
    send_loc = updt_loc
    if updt_loc:
        location = three_digit_str(cur_loc)
        updt_loc = False

    send_color = updt_color
    if updt_color is True:
        color_index = (color_index+1)%3
        print('index: ', color_index)
        updt_color = False
        
    send_pos = updt_pos
    if updt_pos:
        if player < 300:
            prev_player = player
            player += 1
        else:
            print('You have won the game') # write win state
        updt_pos = False

def check_inputs(self):
    x_axis = joystick.get_axis(0)
    x_btn = joystick.get_button(0)
    a_btn = joystick.get_button(1)
    l_trig = joystick.get_button(4)
    
    if (x_axis > 0.5):
        updt_loc = True
        cur_loc = (cur_loc + 4)%96
    elif(x_axis <-0.5):
        updt_loc = True
        cur_loc = (cur_loc - 4)%96
    
    if(x_btn == 1):
        updt_color = True
    
    if(a_btn == 1):
        move = True
        
    if(l_trig == 1):
        reset = True
    
def send_updts(self):
    if send_loc:
        #print(location)
        message = 'GoTo' + location + '\n'
        print(message)
        ser.write(message.encode())
        
    
    if send_color:
        r = three_digit_str(colors[color_index].r)
        g = three_digit_str(colors[color_index].g)
        b = three_digit_str(colors[color_index].b)
        message = 'L' + three_digit_str(5) + ',' + r + ',' + g + ',' + b + '\n'
        print(message)
        ser.write(message.encode())
    
    if send_pos:
        message_off = 'M' + three_digit_str(prev_player) + ',000,000,000\n'
        message_on = 'M' + three_digit_str(player) + ',050,050,050\n'
        print(message_off)
        print(message_on)
        ser.write(message_off.encode())
        time.sleep(0.16)
        ser.write(message_on.encode())
        prev_player = player
        
def send_reset(self):
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
    
def update_game(self, ser):
    if (first_run == 1):
        time.sleep(10)
        print("Done")
        first_run = 0
        
    update_values()
    check_inputs()
    send_messages()
    
    
    if reset:
        send_reset()
        
    reset = False
