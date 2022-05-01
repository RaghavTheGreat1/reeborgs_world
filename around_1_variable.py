# Initial position of bot of x axis
initial_x = 4
# Number of columns
x = 10
# Number of row
y = 9

for i in range(initial_x,  (2*x) + (2*y) + initial_x, 1):
    if(front_is_clear()):
        move()
    else: 
        turn_left()
