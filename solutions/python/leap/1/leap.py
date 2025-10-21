def leap_year(year):
    """
    This fuction is getting year and checking if it is evenly devided by 4 
    and 400 in case it's evenly devided by 100
    """

    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return False
    return True
