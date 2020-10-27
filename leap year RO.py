def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    if a_year % 400 == 0:
        return True
    if a_year % 100 == 0:
       return False
    else:
        return False
print(is_leap_year(2000))
   
       

    
       

    
    





