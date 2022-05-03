def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def u_turn():
    turn_left()
    turn_left()

number_of_leaves = 0
# Take the leaves 
while front_is_clear():
    move()
    while object_here():
        take()  
        number_of_leaves = number_of_leaves + 1

u_turn()

# Drop the leaves
while front_is_clear():
    move()
turn_right()
while number_of_leaves > 0:
    toss()
    number_of_leaves = number_of_leaves - 1
