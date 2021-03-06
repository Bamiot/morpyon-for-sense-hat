from sense_hat import SenseHat
from time import sleep as wait
from AI import morpyon
#from morpyon.AI import morpyon

sense = SenseHat()
sense.clear()
sense.low_light = True

activate_ai = True

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [127, 127, 0]
cyan = [0, 137, 127]
magenta = [127, 0, 127]

white = [255, 255, 255]
low_white = [160, 140, 180]
blank = [50, 50, 0]
off = [0, 0, 0]

global player


def main():
    global player

    grid = [[[50, 50, 0], [50, 50, 0], [50, 50, 0]],
            [[50, 50, 0], [50, 50, 0], [50, 50, 0]],
            [[50, 50, 0], [50, 50, 0], [50, 50, 0]]]

    m_grid = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    selected = [1, 1]

    line = off

    player = 1

    ai = morpyon(m_grid, activate_ai)

    def grid_to_grid():
        for i in range(3):
            for ii in range(3):
                if m_grid[i][ii] == 1:
                    grid[i][ii][0] = 255
                    grid[i][ii][1] = 0
                elif m_grid[i][ii] == 2:
                    grid[i][ii][1] = 255
                    grid[i][ii][0] = 0
                else:
                    grid[i][ii][0] = 50
                    grid[i][ii][1] = 50

    def update_grid():
        grid_to_grid()
        matrix = [
            grid[0][0], grid[0][0], line, grid[0][1], grid[0][1], line, grid[0][2], grid[0][2],
            grid[0][0], grid[0][0], line, grid[0][1], grid[0][1], line, grid[0][2], grid[0][2],
            line, line, line, line, line, line, line, line,
            grid[1][0], grid[1][0], line, grid[1][1], grid[1][1], line, grid[1][2], grid[1][2],
            grid[1][0], grid[1][0], line, grid[1][1], grid[1][1], line, grid[1][2], grid[1][2],
            line, line, line, line, line, line, line, line,
            grid[2][0], grid[2][0], line, grid[2][1], grid[2][1], line, grid[2][2], grid[2][2],
            grid[2][0], grid[2][0], line, grid[2][1], grid[2][1], line, grid[2][2], grid[2][2]
        ]
        sense.set_pixels(matrix)

    def pushed_up():
        selected[0] = (selected[0] - 1) % 3

    def pushed_left():
        selected[1] = (selected[1] - 1) % 3

    def pushed_down():
        selected[0] = (selected[0] + 1) % 3

    def pushed_right():
        selected[1] = (selected[1] + 1) % 3

    def deselect():
        for i in range(3):
            for ii in range(3):
                grid[i][ii][2] = 0

    def select():
        deselect()
        grid[selected[0]][selected[1]][2] = 255

    def is_full():
        for i in range(3):
            for ii in range(3):
                if m_grid[i][ii] == 0:
                    return False
        return True

    def is_win():
        for i in range(3):
            if m_grid[i][0] == m_grid[i][1] == m_grid[i][2] != 0:
                return True
            elif m_grid[0][i] == m_grid[1][i] == m_grid[2][i] != 0:
                return True
        if m_grid[0][0] == m_grid[1][1] == m_grid[2][2] != 0:
            return True
        elif m_grid[2][0] == m_grid[1][1] == m_grid[0][2] != 0:
            return True
        else:
            return False

    def win(pl):
        colo = white
        deselect()
        update_grid()
        wait(1)
        if pl == 2:
            print("vert ai gagne")
            colo = green
        elif pl == 1:
            print("rouge player gagne")
            colo = red
        elif pl == 0:
            print("egaliter")
        for i in range(5):
            sense.clear(colo)
            wait(0.15)
            sense.clear()
            wait(0.15)

    def turn(pl):
        global player
        if pl == 1:
            player = 2
        elif pl == 2:
            player = 1

    def pushed_middle():

        if m_grid[selected[0]][selected[1]] == 0:
            m_grid[selected[0]][selected[1]] = player
            update_grid()

            if ai.activated:
                wait(0.3)
                if is_win():
                    win(1)
                elif not is_full():
                    xy = ai.play(m_grid)
                    m_grid[xy[0]][xy[1]] = 2
                    update_grid()
                    if is_win():
                        win(2)
                elif is_full():
                    win(0)
            else:
                if is_win():
                    win(player)
                elif is_full():
                    win(0)
                elif not is_full():
                    turn(player)

    update_grid()

    while not is_win() and not is_full():
        for event in sense.stick.get_events():
            # print("joystick was {} {}".format(event.action, event.direction))
            if event.direction == 'up' and event.action == 'pressed':
                pushed_up()
            elif event.direction == 'down' and event.action == 'pressed':
                pushed_down()
            elif event.direction == 'left' and event.action == 'pressed':
                pushed_left()
            elif event.direction == 'right' and event.action == 'pressed':
                pushed_right()
            elif event.direction == 'middle' and event.action == 'pressed':
                pushed_middle()

            if event.action == 'pressed' and not is_win() and not is_full():
                select()
                update_grid()
                #print(m_grid)
                if is_full():
                    deselect()
                    update_grid()


flash_max = 60
flash = 0
time = 0.015
tempo = True
while True:

    while tempo:
        flash = (flash + 1) % flash_max
        wait(time)
        if flash <= (flash_max * 1 / 6):
            sense.clear(red)
        elif flash <= (flash_max * 2 / 6):
            sense.clear(yellow)
        elif flash <= (flash_max * 3 / 6):
            sense.clear(green)
        elif flash <= (flash_max * 4 / 6):
            sense.clear(cyan)
        elif flash <= (flash_max * 5 / 6):
            sense.clear(blue)
        else:
            sense.clear(cyan)

        for event in sense.stick.get_events():
            # print("joystick was {} {}".format(event.action, event.direction))
            if event.direction == 'middle' and event.action == 'pressed':
                tempo = False

    sense.show_message("Morpyon", .06, [0, 255, 0], [50, 50, 50])
    main()