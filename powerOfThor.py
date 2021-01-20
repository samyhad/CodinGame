import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# if(light_x < 0):
#     light_x -= 80
# else:
#     light_x -= 40
#
# if(initial_tx < 0):
#     initial_tx -= 80
# else:
#     initial_tx -= 40
#
# if(light_y < 0):
#     light_y += 36
# else:
#     light_y += 18
#
# if(initial_ty < 0):
#     initial_ty += 36
# else:
#     initial_ty += 18

initial_tx =+ 18
light_x =+ 18

initial_ty =- 40
light_y =- 40

if(initial_tx > light_x):
    x = initial_tx - light_x
else:
    x = light_x - initial_tx

if(initial_ty > light_y):
    y = initial_ty - light_y
else:
    y = light_y - initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug:
    print("x: {} - y: {}".format(x, y), file=sys.stderr, flush=True)

    ang_radious = math.atan2(y, x)
    ang_degrees = (180/math.pi)*ang_radious

    if(ang_degrees == 0 or ang_degrees == 360):
        print("E")
    elif (ang_degrees > 0 and ang_degrees < 90):
        print("NE")
    elif(ang_degrees == 90):
        print("N")
    elif(ang_degrees > 90 and ang_degrees < 180):
        print("NW")
    elif(ang_degrees == 180):
        print("W")
    elif(ang_degrees > 180 and ang_degrees < 270):
        print("SW")
    elif(ang_degrees == 270):
        print("S")
    elif(ang_degrees > 270 and ang_degrees < 360):
        print("SE")

    # A single line providing the move to be made: N NE E SE S SW W or NW
    # print("SE")
