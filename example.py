from Astar import pathfind # import the library when it is in the same folder
# you can also use import Astar but you will need to write Astar.functionName to use it
# if you want to have it in a separate folder use "from folderPath.Astar import pathfind"


# you must have a 2 dimensional list of any size for this to work
map = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
       [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
       [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
       [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],]


# specify the starting coordinates and the end coordinates

startX = 0
startY = 0
endX = 2
endY = 0

# call the function pathfind(map: the 2 dimensional list, startX: the starting x coordinate, startY: the starting y coordinate, endX: the ending x coordinate, endY: the ending y coordinate
#      diagonal: False by default if diagonal movement is allowed, p_maxIterations: 600 by default the max number of iterations before it gives up and returns None and the number of iterations[maxIterations + 1]
#      and 0, returnMap: False by default if it should return the map with the path on it, empty: [0] by default what is considered an empty space)

# returns path: the sequence of instructions to get from start to end, iterations: the number of iterations required to find the path, length: the length of the path

# here we tell it to start at the coordinates startX, startY, to end at endX, endY, and to allow diagonal movement
path, iterations, length = pathfind(map, startX, startY, endX, endY, True)
print(path, iterations, length, "\n\n\n")

# output:
# ['down', 'down', 'down', 'down-right', 'down', 'down', 'down', 'down', 'down-right', 'right', 'right', 'up-right', 'up', 'up', 'up', 'up-right', 'right', 'right', 'down-right', 'up-right', 'up-right', 'up-right', 'up', 'up-left', 'left', 'left', 'left', 'left', 'left', 'left', 'down-left', 'down-left', 'up-left', 'up'] 124 34

# here we tell it to start at the coordinates startX, startY, to end at endX, endY, and not to allow diagonal movement, to have an iteration limit of 800 and to return the map; so path will actually be the map with the path written with "C"s
path, iterations, length = pathfind(map, startX, startY, endX, endY, False, 800, True)
print(path, iterations, length)

# output:
# [['B', 1, 'A', 1, 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 1, 'C', 'C', 'C', 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], ['C', 1, 'C', 1, 'C', 1, 0, 1, 1, 1, 1, 1, 'C', 1, 'C', 1, 'C', 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], ['C', 1, 'C', 'C', 'C', 1, 0, 1, 0, 0, 0, 0, 'C', 'C', 'C', 1, 'C', 'C', 'C', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['C', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 'C', 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], ['C', 'C', 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 'C', 'C', 'C', 'C', 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], [0, 'C', 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 'C', 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 'C', 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 'C', 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 'C', 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 'C', 'C', 'C', 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 'C', 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 'C', 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0], [1, 'C', 'C', 'C', 'C', 1, 1, 0, 0, 1, 1, 0, 0, 'C', 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], [1, 0, 1, 0, 'C', 1, 0, 0, 1, 0, 0, 0, 0, 'C', 'C', 'C', 'C', 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 'C', 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 'C', 'C', 'C', 'C', 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 'C', 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 'C', 1, 0, 0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 'C', 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 'C', 1, 1, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 'C', 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 'C', 'C', 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 'C', 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 'C', 'C', 0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 'C', 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 'C', 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 'C', 'C', 'C', 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 'C', 'C', 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1, 'C', 'C', 'C', 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 'C', 1, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 0, 1, 'C', 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 'C', 'C', 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 0, 1, 'C', 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 'C', 1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0, 1, 'C', 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 'C', 1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0, 1, 'C', 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 'C', 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0, 0, 0, 'C', 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 'C', 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 1, 0, 0, 'C', 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 'C', 0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0, 'C', 'C', 'C', 1, 1, 0, 0, 0, 0, 1, 0, 1, 'C', 'C', 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]] 473 112