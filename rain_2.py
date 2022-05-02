def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
move()
move()
move()
turn_right()
move()

# Functions that is being used in toWall() to get back to the initial position after completing the inspection
def u_turn():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    
# Functions that will check whether to wall the cleared right path or not by going through the next step and returning to tell a confirmed result
def toWall():
    move()
    if(right_is_clear()):
        u_turn()
        return False
    else:
        u_turn()
        return True

# Main iterative that builds wall wherever required  
while not at_goal():
    if(right_is_clear() and front_is_clear()):
        if(toWall()):
            turn_right()
            build_wall()
            turn_left()
        else:
            turn_right()
            move()
            
    elif(front_is_clear() and not right_is_clear()):
        move()
    else: 
        turn_left()
    
     
