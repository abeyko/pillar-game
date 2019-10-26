import Character.py

first_run = 1
loc_str = '000'
cur_loc = 0
updt_loc = False
color_index = 0
updt_color = False
player = 0
prev_player = 0
move = False
reset = True


def update_game(self, ser):
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
        
    if ( first_run == 1):
        time.sleep(10)
        print("Done")
        first_run = 0
        
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
