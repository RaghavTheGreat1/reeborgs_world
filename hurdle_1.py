def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_and_left():
    move()
    turn_left()
    
def move_and_right():
    move()
    turn_right()
    
# Observations: 
# (x, 1) -> move -> turn left 
# (x, 2) -> move -> turn Right

def jump():
    move_and_left()
    move_and_right()
    move_and_right()
    move_and_left()

for i in range(0, 6, 1):
    jump()
    
