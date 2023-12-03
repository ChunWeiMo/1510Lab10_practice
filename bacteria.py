import sys


def colonize(width, height, x_coordinate, y_coordinate, max_generation):
    if width <= 0 or height <= 0:
        raise ValueError('Width and heigh must be greater than 0.')
    if x_coordinate < 0 or x_coordinate >= width:
        raise ValueError('X-Coordinate must be between [0, width-1].')
    if y_coordinate < 0 or y_coordinate >= height:
        raise ValueError('Y-Coordinate must be between [0, height-1].')
    if max_generation < 0:
        raise ValueError('Maximum desired generation must be greater than 0.')
    surface = dict()
    for row in range(height):
        for column in range(width):
            surface[(column, row)] = False
    print(surface)
    spread_like_bacteria(surface, (x_coordinate, y_coordinate), max_generation)
    print(surface)
    return surface


def spread_like_bacteria(surface, coordinate, max_generation):
    """

    """
    if max_generation >= 0:
        try:
            surface[coordinate]
        except TypeError:
            print("Surface must be a dictionary.")
        except KeyError:
            print(f'A bacteria is outside boundary.')
        else:
            if not surface[coordinate] :
                surface[coordinate] = True
                spread_like_bacteria(surface, (coordinate[0], coordinate[1]-1), max_generation-1)
                spread_like_bacteria(surface, (coordinate[0], coordinate[1]+1), max_generation-1)
                spread_like_bacteria(surface, (coordinate[0]-1, coordinate[1]), max_generation-1)
                spread_like_bacteria(surface, (coordinate[0]+1, coordinate[1]), max_generation-1)


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
    width += 1
    height += 1

    for row in range(height):
        for column in range(width):
            if surface[(column, row)]:
                print('*', end='')
            else:
                print('0', end='')
        print()


def check_argv(argv):
    if len(argv) < 6:
        raise IndexError('Need 5 command line arguments with this program.')
    print(type(argv[2]))


def main(argv):
    """
    Drive this program.
    """
    try:
        width, height, x_coordinate, y_coordinate, max_generation = int(
        argv[1]), int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5])
    except (IndexError, ValueError):
        print('Need 5 integer as command line arguments to start experiment.')
        print('Experiment does not start.')
        return
    try:
        surface = colonize(width, height, x_coordinate, y_coordinate, max_generation)
    except ValueError as e:
        print(e)
    else:
        print_surface(surface)
    

if __name__ == '__main__':
    # main(sys.argv)
    surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
               (1, 1): False, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
    coordinate = (1, 1)
    max_generation = 2
    spread_like_bacteria(surface, coordinate, max_generation)
    print(surface)
