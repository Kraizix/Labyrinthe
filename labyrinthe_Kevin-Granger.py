# Program that creates a random maze with user's input dimensions (with a minimum of 8*8 else it will cause some
# infinite loop during the paths creation). Sometimes the program may not work correctly, particularly on small grid
# between 8*8 and 10*10, it might cause some infinite loops. The program has better results on wide grid (greater than
# 25*25) Also you can play on the labyrinth, you are spawning on the S square and you can navigate through the
# labyrinth using N,E,S,W directions(North,East,South,West) your goal is to find the exit which is hidden or not
# based on your choices (To play on the labyrinth I highly recommend to play on a large grid, 25*25 minimum,
# else it will not be really interesting to test it)

from random import randint


def make_lab(width, height):
    return [['W' for _ in range(width)] for _ in range(height)]


def print_lab(lab):
    for row in lab:
        print(",".join(row))
    print("")


def create_lab(lab_width, lab_height, lab):
    start_x = randint(1, lab_width - 1)
    start_y = randint(1, lab_height - 1)
    end_x = randint(1, lab_width - 1)
    end_y = randint(1, lab_height - 1)
    while end_x == start_x and end_y == start_y:
        end_x = randint(1, lab_width - 1)
        end_y = randint(1, lab_height - 1)
    lab[start_x][start_y] = 'S'
    lab[end_x][end_y] = 'A'
    replace_wall(start_x, start_y, end_x, end_y, lab)
    path_number = 5
    if lab_width * lab_height > 200:
        path_number = 15
    for _ in range(path_number):
        path_x = randint(1, lab_width - 2)
        path_y = randint(1, lab_height - 2)
        path_end_x = randint(1, lab_width - 2)
        path_end_y = randint(1, lab_height - 2)
        while path_end_x == start_x and end_y == start_y:
            path_end_x = randint(1, lab_width - 2)
            path_end_y = randint(1, lab_height - 2)
        while lab[path_x][path_y] != " ":
            path_x = randint(1, lab_width - 2)
            path_y = randint(1, lab_height - 2)
        replace_wall(path_x, path_y, path_end_x, path_end_y, lab)
    return start_x, start_y, end_x, end_y


def replace_wall(first_x, first_y, last_x, last_y, lab):
    temp_x = first_x
    temp_y = first_y
    while True:
        if temp_x > last_x:
            temp_x -= 1
            if temp_x == last_x and temp_y == last_y:
                break
            else:
                if lab[temp_x][temp_y] == 'W' or lab[temp_x][temp_y] == ' ':
                    lab[temp_x][temp_y] = ' '
                else:
                    break
        elif temp_x < last_x:
            temp_x += 1
            if temp_x == last_x and temp_y == last_y:
                break
            else:
                if lab[temp_x][temp_y] == 'W' or lab[temp_x][temp_y] == ' ':
                    lab[temp_x][temp_y] = ' '
                else:
                    break
        elif temp_y > last_y:
            temp_y -= 1
            if temp_x == last_x and temp_y == last_y:
                break
            else:
                if lab[temp_x][temp_y] == 'W' or lab[temp_x][temp_y] == ' ':
                    lab[temp_x][temp_y] = ' '
                else:
                    break
        elif temp_y < last_y:
            temp_y += 1
            if temp_x == last_x and temp_y == last_y:
                break
            else:
                if lab[temp_x][temp_y] == 'W' or lab[temp_x][temp_y] == ' ':
                    lab[temp_x][temp_y] = ' '
                else:
                    break


def is_movement_possible(player_x, player_y, direction, lab):
    directions_list = {'N', 'E', 'S', 'W'}
    if direction not in directions_list:
        return False
    elif direction == 'N':
        if lab[player_x - 1][player_y] == "W":
            return False
    elif direction == 'E':
        if lab[player_x][player_y + 1] == "W":
            return False
    elif direction == 'S':
        if lab[player_x + 1][player_y] == "W":
            return False
    elif direction == 'W':
        if lab[player_x][player_y - 1] == "W":
            return False
    return True


x = int(input("Choose a width for your maze : (it must be greater than 7) "))
while x <= 7:
    x = int(input("Incorrect value, please choose a width value greater than 7 : "))
y = int(input("Choose a height for your maze : (it must be greater than 7) "))
while y <= 7:
    y = int(input("Incorrect value, please choose a height value greater than 7 : "))
lab = make_lab(x, y)
player_x, player_y, exit_x, exit_y = create_lab(x, y, lab)
wanna_play = input(
    "Wanna play on the grid, type Yes or Y else if you  just want to print the grid type any other characters : ")
if wanna_play == "Y" or wanna_play == "Yes":
    invisible_exit = input(
        "Do you want to display the exit on the labyrinth or not, type Yes or Y if you want to, if you don't want put "
        "any other characters : ")
    if invisible_exit == "Y" or wanna_play == "Yes":
        lab[exit_x][exit_y] = " "
    print_lab(lab)
    first = True
    while True:
        if first:
            print(
                'Well you finally entered the labyrinth, you are currently on the S square and you can navigate '
                'through the labyrinth using N,E,S,W directions, the exit is hidden in one of the square and you can '
                'navigate through the labyrinth using N,E,S,W directions of the grid find it to leave the labyrinth')
        direction = input("select a direction (N,E,S,W) to move your character : ")
        while not is_movement_possible(player_x, player_y, direction, lab):
            print("The direction you put is not possible")
            direction = input("select a direction (N,E,S,W) to move your character : ")
        if not first:
            lab[player_x][player_y] = ' '
        else:
            first = False
        if direction == 'N':
            player_x -= 1
        if direction == 'E':
            player_y += 1
        if direction == 'S':
            player_x += 1
        if direction == 'W':
            player_y -= 1
        if player_x == exit_x and player_y == exit_y:
            lab[exit_x][exit_y] = 'A'
            print_lab(lab)
            print("Congratulations you escaped the labyrinth")
            break
        lab[player_x][player_y] = 'X'
        print_lab(lab)
else:
    print_lab(lab)
