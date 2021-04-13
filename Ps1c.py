def FloatConvention(a):
    """
    Assumes that a is an int.
    Divides big numbers into chunks of thirds. For example: 1200000 -> 1.200.000 where 12000000 = 1.200.000
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
    """
    Takes 2 inputs, your annual_salary and cost of your dream house. 
    Returns whether it's possible to gather enough money to buy the house in 36 months. If possible, returns the percentage of your annual salary for a month that gets you to buy the house.
    """
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
    #Flag = False
    
    while True:
    #Initials   
        month = 1
        current_savings = 0.0
        starting_annual_salary = annual_salary
        portion_saved = portion_saved_int / 10000
        step += 1
        if portion_saved == 1.0:
            Flag = True
        print(portion_saved_int, portion_saved, annual_salary)
        #print(f"monthly saved: {monthly_saved}")
        
        while month <= 36:
            monthly_money = (starting_annual_salary / 12) * portion_saved
            current_savings += monthly_money + ((current_savings * r) / 12)
            if month % 6 == 0:
                starting_annual_salary += starting_annual_salary * semi_annual_salary
                #print(f"monthly_money{monthly_money}, starting_annual_salary: {starting_annual_salary}")
            print(f"current saving: {current_savings}, difference: {portion_down_payment - current_savings} ")
            month += 1
       
        if Flag == True and current_savings < portion_down_payment:
           print(r"It's not possible to pile up that amount of money in 36 months. Also you --> (╯°□°）╯")
           return None
        if current_savings < portion_down_payment:
            bot = portion_saved_int
        elif current_savings > portion_down_payment:
            top = portion_saved_int
        if abs(current_savings - portion_down_payment) < eps:
            break
        portion_saved_int = (top + bot) // 2 
        Flag = False
    return (portion_saved, step)
print(Pset1())
