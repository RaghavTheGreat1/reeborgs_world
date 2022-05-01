# initial postion of bot in x axis
initial_x = 4
# number of columns
x = 10
# number of rows
y = 10

def turn_right():
    turn_left()
    turn_left()
    turn_left()

for i in range(initial_x,  (2*x) + (2*y) + initial_x + 1, 1):
    if(front_is_clear() and right_is_clear() == False):
        move()
    elif right_is_clear(): 
        turn_right()
        move()
    else:
        turn_left()
        
        
