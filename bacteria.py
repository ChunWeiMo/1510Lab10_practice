def colonize(width, height, x_coordinate, y_coordinate, max_generation):
    surface = dict()
    for row in range(height+1):
        for column in range(width+1):
            surface[(column, row)] = False
    spread_like_bacteria(surface, (x_coordinate, y_coordinate), max_generation)
    # print(surface)
    return surface


def spread_like_bacteria(surface, coordinate, max_generation):
    """

    """
    try:
        surface[coordinate]
    except KeyError:
        print('The coordinate is outside of the surface.')
    else:
        if (not surface[coordinate]) and max_generation >= 0:
            surface[coordinate] = True
            spread_like_bacteria(
                surface, (coordinate[0], coordinate[1]-1), max_generation-1)
            spread_like_bacteria(
                surface, (coordinate[0], coordinate[1]+1), max_generation-1)
            spread_like_bacteria(
                surface, (coordinate[0]-1, coordinate[1]), max_generation-1)
            spread_like_bacteria(
                surface, (coordinate[0]+1, coordinate[1]), max_generation-1)


def check_populated():
    """
    11. You may wish to create a helper function that accepts a reference to the surface and a proposed set of coordinates 
    returns False if the coordinates are valid and/or already populated
    returns True if the location is ripe for colonization.
    """
    pass


def print_surface(surface):
    width, height = 0, 0
    for coordinate in surface:
        if coordinate[0] > width:
            width = coordinate[0]            
        if coordinate[1] > height:
            height = coordinate[1]
            
    for row in range(height):
        for column in range(width):
            if surface[(column, row)]:
                print('*', end='')
            else:
                print('0', end='')
        print()


def main():
    surface = colonize(11, 11, 5, 5, 3)
    print_surface(surface)


if __name__ == '__main__':
    main()
