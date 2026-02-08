def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
  
while not is_facing_north():
    turn_left()
turn_right()

while not at_goal():
    while front_is_clear() and not at_goal():
        move()
        if right_is_clear() and not is_facing_north():
            turn_right()
            
    if wall_in_front() and wall_on_right():
        if is_facing_north():
            turn_around()
        elif right_is_clear():
            turn_around()
        else:
            turn_left()

    elif wall_in_front() and right_is_clear():
        turn_right()
    



