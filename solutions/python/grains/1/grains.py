def square(number):
    """
    Function designed to do ariphmetical progression from 1 to 64
    ariphmetical progression starts with 1; if number exceeds 64 or
    less than 0 -- it's considered to be out of size and therefore excepted
    """
    grains_on_square = 1
    # Out-Of-Range exception:
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    
    # Calculating ammount of grains on given square:
    for i in range(number - 1):
        grains_on_square += grains_on_square
    return grains_on_square

def total():
    """
    This is a hardcoded value of total ammount of grains with ariphmetical
    prgoression. This function does not accept any variable therefore it's hardcoded
    """
    return 18446744073709551615
