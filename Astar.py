from math import sqrt

def clamp(n, minV, maxV):
    return min(maxV, max(n, minV))

def distance(x1, y1, x2, y2, diagonal=False):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def pathfind(p_map, startX, startY, endX, endY, diagonal=False, p_maxIterations=600, returnMap=False, empty=[0]):
    iterations = 0
    maxIterations = p_maxIterations

    selX = endX
    selY = endY

    map = p_map.copy()

    if not diagonal:
        moves = [[1, 0, "up"], [-1, 0, "down"], [0, 1, "left"], [0, -1, "right"]]
    else:
        moves = [[1, 0, "up"], [-1, 0, "down"], [0, 1, "left"], [0, -1, "right"], [1, 1, "up-left"], [1, -1, "up-right"], [-1, 1, "down-left"], [-1, -1, "down-right"]]

    mapValues = []
    for i, y in enumerate(map):
        mapValues.append([])
        for x in y:
            mapValues[i].append({"path": "left", "f": 0, "g": 0, "h": 0, "explored": False})

    while iterations < maxIterations:
        if selX == startX and (selY == startY):
            break

        mapValues[selY][selX]["explored"] = True
        map[selY][selX] = 2

        sel = mapValues[clamp(selY, 0, len(map) - 1)][clamp(selX, 0, len(map[selY]) - 1)]

        for i in moves:
            locationY = clamp(selY + i[0], 0, len(map) - 1)
            locationX = clamp(selX + i[1], 0, len(map[clamp(selY + i[0], 0, len(map) - 1)]) -1)
            selSearch = mapValues[locationY][locationX]
            if map[locationY][locationX] in empty and not selSearch["explored"]:
                if (sel["g"] + 1 + distance(selX + i[1], selY + i[0], endX, endY)) < selSearch["f"] or (selSearch["f"] == 0):
                    if i[0] and i[1]:
                        selSearch["g"] = sel["g"] + 1.4
                    else:
                        selSearch["g"] = sel["g"] + 1
                    selSearch["h"] = distance(selX + i[1], selY + i[0], endX, endY, diagonal)
                    selSearch["f"] = selSearch["g"] + selSearch["h"]
                    selSearch["path"] = i[2]
        
        lowestF = 0
        for iy, y in enumerate(mapValues):
            for ix, x in enumerate(y):
                if (lowestF == 0 or (x["f"] < lowestF)) and (x["f"] != 0) and (not x["explored"]):
                    lowestF = x["f"]
                    selX = ix
                    selY = iy

        iterations += 1

    length = 0
    if iterations >= maxIterations:
        print("path not found within iteration limit")
        return None, iterations, length
    
    map[selY][selX] = "B"
    path = []
    while (selX != endX) or (selY != endY):
        path.append(mapValues[selY][selX]["path"])
        if mapValues[selY][selX]["path"] == "right":
            selX += 1
        elif mapValues[selY][selX]["path"] == "left":
            selX -= 1
        elif mapValues[selY][selX]["path"] == "up":
            selY -= 1
        elif mapValues[selY][selX]["path"] == "down":
            selY += 1
        elif mapValues[selY][selX]["path"] == "up-left":
            selY -= 1
            selX -= 1
        elif mapValues[selY][selX]["path"] == "up-right":
            selY -= 1
            selX += 1
        elif mapValues[selY][selX]["path"] == "down-left":
            selY += 1
            selX -= 1
        elif mapValues[selY][selX]["path"] == "down-right":
            selY += 1
            selX += 1
        map[selY][selX] = "C"
        length += 1
        if length > maxIterations:
            break
    map[selY][selX] = "A"

    if returnMap:
        return map, iterations, length
    else:
        return path, iterations, length