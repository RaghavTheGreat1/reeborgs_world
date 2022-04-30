def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_and_left():
    move()
    turn_left()

    
def right_and_move():
    turn_right()
    move()
    
def left_and_move():
    turn_left()
    move()
    
# Observations: 
# jump when wall is next to it
# reposition to normal after jump

def jump():
    left_and_move()
    right_and_move()
    right_and_move()
    turn_left()
    
while at_goal() == False:
    move()
    jump()

    
    
    
