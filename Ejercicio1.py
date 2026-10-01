import math

donas = {
    i: math.sqrt(2) ** (i - 1)
    for i in range(1, 11)
}

print (donas)
