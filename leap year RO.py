def is_leap_year(a_year):

    if a_year % 4 == 0:
        return True
        print ('is leap year')
    elif a_year % 100 == 0:
        return False
        print ('is not leap year')
    elif a_year % 400 == 0:
        return True
        print ('is leap year')
    else: 
        return False    
    
    print(is_leap_year(1998))





