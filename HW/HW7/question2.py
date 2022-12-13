def move_robot(n):
    pos = [0,0]
    for i in range(-1, n):
        if i == -1:
            yield tuple(pos)
        else:
            face = (i) % 4
            if face == 0:
                # move north
                pos[1] += (i + 1)
            elif face == 1:
                # move east
                pos[0] += (i + 1)
            elif face == 2:
                # move south
                pos[1] -= (i + 1)
            else:
                # move west
                pos[0] -= (i + 1)
            i += 1
            yield tuple(pos)

