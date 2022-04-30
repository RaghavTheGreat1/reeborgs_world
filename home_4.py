def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def first_l():
    for i in range(0, 7, 1):
        if(i == 3):
            turn_left()
            move()
        elif(i==6):
            turn_right()
        else:
            move()
        
for i in range(0, 4, 1):
    first_l()
    if(i!=3):
        move()
        turn_right()
