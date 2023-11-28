def colonize(width, height, x_coordinate, y_coordinate):
    surface = dict()
    for column in range(width):
        for row in range(height):
            surface[(column, row)] = False
    print(surface)


def spread_like_bacteria(surface, coordinate: tuple):
    try:
        surface[coordinate]
    except KeyError:
        print('The coordinate is outside of the surface.')
    else:
        surface[coordinate] = True
    
    
def main():
    colonize(7, 3, 1, 1)
  

if __name__ == '__main__':
    main()