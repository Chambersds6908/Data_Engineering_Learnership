def maximum(*numbers):
    currentmax = 0
    for n in numbers:
        if n > currentmax:
            currentmax = n
    return currentmax

maximum(1,9,2,300,3)

