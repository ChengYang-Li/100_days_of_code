#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

count = 0
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        count += 1
        if count == 4:
            turn_left()
    elif front_is_clear():
        count = 0
        move()
    else:
        count = 0
        turn_left()
     

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
