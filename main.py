def Calculate_yearly_multiple(pay_interval:str)->int:
    match (pay_interval):
        case "monthly":
            yearly_multiple=12
        case "biweekly":
            yearly_multiple=26
        case "weekly":
            yearly_multiple=52
        case default:
            print("Please enter a valid interval of payment of ")
            pay_interval=input("How do you get payed? \ne.g monthly, weekly, biweekly: ").lower()
            yearly_multiple=Calculate_yearly_multiple(pay_interval)
    return yearly_multiple

def Calculate_yearly_salary(pay_interval:str,pay: float)-> float:
    """
    calculates the gross yearly pay
    
    Parameters:
        pay_interval(str): How often the user gets payed
        pay(float): How much they are payed based on pay_interval
        
    Returns:
        float: A floating point number with that is the yearly salary
    """

    return pay*Calculate_yearly_multiple(pay_interval)
    
def Calculate_tax_per_interval(income: float, yearly_multiple:int, chargible_income: float):
    
    if chargible_income <=5000:
        tax= 0.1 * (chargible_income/yearly_multiple)
        
    elif chargible_income<=10000:
        excess=chargible_income-5000
        tax=(1/yearly_multiple)*(500+0.2*excess)
        
    elif chargible_income>10000:
        excess=chargible_income-10000
        tax=(1/yearly_multiple)*(1500+0.28*excess)
        
    
    print("Calculate tax =",tax)
    return '{:.2f}'.format(tax)

def Calculate_financess(yearly_salary, chargible_income,yearly_multiple,pay_interval,tax_per_interval, currency):
    
    print(f"Yearly gross salary is:{currency}{yearly_salary}")
    print(f"Yearly chargible income is:{currency}{chargible_income}")
    print(f"{pay_interval.capitalize()} chargible income is:{currency}{chargible_income/yearly_multiple}")
    print(f"{pay_interval.capitalize()} salary is : {currency}{yearly_salary/yearly_multiple}")
    print(f"{pay_interval.capitalize()} tax is : {currency}{tax_per_interval}")
    print(f"Yealry tax is : {currency}{float(tax_per_interval)*yearly_multiple}")
    
def main():
    STANDARD_DEDUCTION=25000

    pay_interval=input("How do you get payed? \ne.g monthly, weekly, biweekly: ").lower()
    pay=float(input("Enter your pay for the above method:"))
    
    yearly_salary=Calculate_yearly_salary(pay_interval,pay)
    chargible_income=yearly_salary-STANDARD_DEDUCTION
    
    yearly_multiple=Calculate_yearly_multiple(pay_interval)
    tax_per_interval=Calculate_tax_per_interval(yearly_salary,yearly_multiple, chargible_income)
    
    Calculate_financess(yearly_salary,chargible_income,yearly_multiple ,pay_interval,tax_per_interval,"EC$")
    
main()