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
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = input('Enter the cost of your dream home: ')
    if 'k' in total_cost:
        print("k in total cost")
        if total_cost[len(total_cost)-1] == 'k':
            print("k in total cost")
            total_cost = float(total_cost[: len(total_cost)-1]) * 1000
        else: 
            raise TypeError('k is only allowed at the end of the string.') 
    elif not 'k' in total_cost: 
        try:
            print('total cost --> float')
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
            print('annual_salary --> float')
            annual_salary = float(annual_salary)
        except:
            print("You didn't type an int or a string (╯°□°）╯")
    print(type(total_cost), type(annual_salary))
    current_savings = 0.0
    r = 0.04
    monthly_annual = annual_salary/12 * portion_saved
    portion_down = 0.25
    portion_down_payment = total_cost* portion_down
    month = 0

    while current_savings < portion_down_payment:
        current_savings += monthly_annual + (current_savings*r)/12 
        month += 1

    return (month , FloatConvention(annual_salary), FloatConvention(total_cost))

print(Pset1())
