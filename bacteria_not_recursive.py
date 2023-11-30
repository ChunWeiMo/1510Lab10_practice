import sys
from bacteria import print_surface


def colonize(width, height, x_coordinate, y_coordinate, max_generation):
    if width <= 0 or height <= 0:
        raise ValueError('Width and heigh must be greater than 0.')
    if x_coordinate <= 0 or x_coordinate > width:
        raise ValueError('X-Coordinate must be between [0, width].')
    if y_coordinate <= 0 or y_coordinate > height:
        raise ValueError('Y-Coordinate must be between [0, height].')
    if max_generation < 0:
        raise ValueError('Maximum desired generation must be greater than 0.')
    surface = dict()
    for row in range(height+1):
        for column in range(width+1):
            surface[(column, row)] = False
    spread_breadth_first(surface, (x_coordinate, y_coordinate), max_generation)
    return surface


def spread_breadth_first(surface, coordinate, max_generation):
    queue, visited = [(coordinate, 0)], set()
    while queue:
        (x_coordinate, y_coordinate), generation = queue.pop(0)
        if generation > max_generation:
            break
        if (x_coordinate, y_coordinate) not in visited:
            surface[(x_coordinate, y_coordinate)] = True
            if (x_coordinate, y_coordinate-1) in surface and (x_coordinate, y_coordinate-1) not in visited:
                queue.append(((x_coordinate, y_coordinate-1), generation+1))
            if (x_coordinate-1, y_coordinate) in surface and (x_coordinate-1, y_coordinate) not in visited:
                queue.append(((x_coordinate-1, y_coordinate), generation+1))
            if (x_coordinate, y_coordinate+1) in surface and (x_coordinate, y_coordinate+1) not in visited:
                queue.append(((x_coordinate, y_coordinate+1), generation+1))
            if (x_coordinate+1, y_coordinate) in surface and (x_coordinate+1, y_coordinate) not in visited:
                queue.append(((x_coordinate+1, y_coordinate), generation+1))
        visited.add((x_coordinate, y_coordinate))


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
        surface = colonize(width, height, x_coordinate,
                           y_coordinate, max_generation)
    except ValueError as e:
        print(e)
    else:
        print_surface(surface)


if __name__ == '__main__':
    main(sys.argv)
