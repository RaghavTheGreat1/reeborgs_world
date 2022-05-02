def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear() and right_is_clear() == False:
        move()
    else:
        if(right_is_clear()):
            turn_right()
            move()
        else:
            turn_left()
    
