def catAndMouse(x, y, z):
    distX = z - x
    distY = y - z
    print(distX)
    print(distY)
    if distX < 0:
        distX = -distX
    if distY < 0:
        distY = -distY
    print(distX)
    print(distY)

    if distX > distY:
        return 'Cat B'
    elif distX < distY:
        return 'Cat A'
    else:
        return 'Mouse C'


print(catAndMouse(85,66,80))
