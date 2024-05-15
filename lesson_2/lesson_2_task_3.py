def square(side_square):
    side_square = side_square * side_square
    if side_square % 1 != 0:
        import math
        side_square = math.ceil(side_square)
        return side_square
    else:
        return side_square
    
print(square(8)) #пример с целым числом
print(square(8.66)) #пример с дробным числом
