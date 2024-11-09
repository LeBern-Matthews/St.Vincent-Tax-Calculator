STANDARD_DEDUCTION=25000

pay_interval=input("How do you get payed? \ne.g monthly, weekly, biweekly: ").lower()
pay=float(input("Enter your pay for the above method:"))


def Calculate_yearly_multiple(pay_interval:str)->int:
    while True:
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
    return yearly_multiple

def Calculate_yearly_salery(pay_interval:str,pay: float)-> float:
    """
    calculates the gross yearly pay
    
    Parameters:
        pay_interval(str): How often the user gets payed
        pay(str): How much they are payed based on pay_interval
        
    Returns:
        float: A floating point number with that is the yearly salery
    """
        
    return pay*Calculate_yearly_multiple(pay_interval)
    
def Calculate_finances(income: float, currency:str, yearly_multiple:int):
    chargible_income=income-STANDARD_DEDUCTION

    print(f"The chargible income is {currency}{chargible_income}")
    
    if chargible_income <=5000:
        tax=0.1*chargible_income
        return tax
    elif chargible_income<=10000:
        excess=chargible_income-5000
        excess_per=excess/yearly_multiple
        print(excess_per)
        tax=(500/yearly_multiple)+(0.2*excess_per)
        return tax
    elif chargible_income>10000:
        excess=chargible_income-10000
        excess_per=excess/yearly_multiple
        print(excess_per)
        tax=(1500/yearly_multiple)+(0.28*excess_per)
        return tax
    
    
print(Calculate_finances(Calculate_yearly_salery(pay_interval,pay), "$EC", Calculate_yearly_multiple(pay_interval)))
