def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
move()
turn_right()
move()

# Wall builder
while not at_goal():
    if(right_is_clear()):
        turn_right()
        build_wall()
        turn_left()
    if(front_is_clear()):
        move()
    else: 
        turn_left()
    
     
        
