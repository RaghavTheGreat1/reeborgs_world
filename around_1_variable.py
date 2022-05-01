# Initial position of bot
initial_x = 4
# Number of rows
x = 10
# Number of columns
y = 9

for i in range(initial_x,  (2*x) + (2*y) + initial_x, 1):
    if(front_is_clear()):
        move()
    else: 
        turn_left()
