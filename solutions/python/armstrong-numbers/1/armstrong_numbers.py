def is_armstrong_number(number):
    """
    This function is calculating wether provided number is an armstrong number by 
    powering digit to the power of length of the number and concatinating it with next digit powered to the length of number

    number - number that we want to check to be an armstrong
    """

    digits = [int(digit) for digit in str(number)]
    power = len(str(number))
    armstrong_check = 0

    for i in range(power):
        armstrong_check += digits[i] ** power
    
    if armstrong_check == number:
        return True

    return False
