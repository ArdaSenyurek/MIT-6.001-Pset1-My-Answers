def FloatConvention(a):
    """
    Assumes that a is an int.  
    """
    counter = 1
    a = int(a)
    digit = ''
    while a > 0:
        remainder = a % 10
        if counter % 3 == 0:
            digit = '.' + str(remainder) + digit
        else:
            digit = str(remainder) + digit
        a = a // 10
        counter += 1
    
    if digit[0] == '.':
        digit = digit[1:]
    elif digit[len(digit)-1] == '.':
        digit = digit[:len(digit)]
    return digit

def Pset1():
    annual_salary = input('Enter your annual salary: ')
    #portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = input('Enter the cost of your dream home: ')
    if 'k' in total_cost:
        if total_cost[len(total_cost)-1] == 'k':
            total_cost = float(total_cost[: len(total_cost)-1]) * 1000
        else: 
            raise TypeError('k is only allowed at the end of the string.') 
    elif not 'k' in total_cost: 
        try:
            total_cost = float(total_cost)
        except: 
                print("You didn't type an int or a string (╯°□°）╯")
    if 'k' in annual_salary:
        print('k')
        if annual_salary[len(annual_salary)-1] == 'k':
            annual_salary = float(annual_salary[: len(annual_salary) - 1]) * 1000
        else: 
            raise TypeError("You didn't type an int or a string (╯°□°）╯")
    elif not 'k' in annual_salary:
        try:
            annual_salary = float(annual_salary)
        except:
            print("You didn't type an int or a string (╯°□°）╯")
    r = 0.04
    portion_down = 0.25
    portion_down_payment = total_cost* portion_down
    eps = 100
    top = 10000
    bot = 0
    portion_saved = 0.0
    portion_saved_int = top
    semi_annual_salary = .07
    step = 0
    
    while True:
    #Initials   
        month = 1
        current_savings = 0.0
        starting_annual_salary = annual_salary
        portion_saved_int = (top + bot) // 2 
        portion_saved = portion_saved_int / 10000
        step += 1
        print(portion_saved_int, portion_saved, annual_salary)
        #print(f"monthly saved: {monthly_saved}")
        
        while month <= 36:
            monthly_money = (starting_annual_salary / 12) * portion_saved
            current_savings += monthly_money + ((current_savings * r) / 12)
            if month % 6 == 0:
                starting_annual_salary += starting_annual_salary * semi_annual_salary
                print(f"monthly_money{monthly_money}, starting_annual_salary: {starting_annual_salary}")
            print(f"current saving: {current_savings}, difference: {portion_down_payment - current_savings} ")
            month += 1
                
        print('I got out')
        if current_savings < portion_down_payment:
            bot = portion_saved_int
        elif current_savings > portion_down_payment:
            top = portion_saved_int
        if abs(current_savings - portion_down_payment) < eps:
            break
    return portion_saved, step
    #while 1:
    #    portion_saved  = portion_saved_int / 10000
    #    monthly_saved = annual_salary * portion_saved  / 12 
    #    print(f"{portion_saved} bum")
    #    while month <= 36:
    #        print(f"{current_savings} current savings")
    #        current_savings += monthly_saved + (current_savings*r) / 12
    #        if month % 6 == 0:
    #            annual_salary += annual_salary * semi_annual_salary
    #            monthly_saved += annual_salary * portion_saved / 12
    #        month += 1
    #    if current_savings < portion_down_payment:
    #        bot = portion_saved_int 
    #    else: 
    #        top = portion_saved_int
    #    if abs(current_savings - portion_down_payment) <= eps:
    #        break
    #    print(f"max : {top}, min: {bot}")
    #    portion_saved_int = (bot + top) // 2
    #        
    #return portion_saved
print(Pset1())
