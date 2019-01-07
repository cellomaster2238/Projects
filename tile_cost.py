# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile
# it would take to cover a floor plan of width and height, using a cost entered by the user.

def tile_cost(length, height, cost):
    total = length * height * cost
    print('The total cost is ${}'.format(total))

tile_cost(10, 12, 4)