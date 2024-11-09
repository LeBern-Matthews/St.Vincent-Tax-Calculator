# Tax Calculator
This Python program calculates yearly gross salary, taxable income, and tax based on different payment intervals (weekly, biweekly, or monthly). The user inputs their pay amount and pay frequency, and the program determines tax per interval and annually after deducting a standard amount from the income.


## Features
- Calculates yearly salary based on the user's pay frequency (monthly, biweekly, or weekly).
- Applies a standard deduction to determine the chargeable income.
- Calculates tax based on progressive tax brackets.
- Provides a breakdown of the calculated tax and chargeable income per pay interval.

##  Usage
To use this program:

1. Run main() from the script.
2. Enter your pay frequency (e.g., "monthly", "biweekly", or "weekly") and pay the amount.
3. The program will display yearly and interval-based income, taxable income, and tax.

## Functions

```
Calculate_yearly_multiple(pay_interval: str) -> int
```

Calculates the number of pay intervals in a year:

- monthly: 12
- biweekly: 26
- weekly: 52

If the input is invalid, the function prompts for valid input.

```
Calculate_yearly_salary(pay_interval: str, pay: float) -> float

```

Calculates yearly gross salary based on the ```pay_interval``` and ```pay```.


```
Calculate_tax_per_interval(income: float, yearly_multiple: int, chargible_income: float) -> str
```

Calculates the tax per pay interval based on progressive tax brackets:

- 10% on income up to 5,000
- 20% on income between 5,001 and 10,000
- 28% on income over 10,000
Returns tax per interval as a formatted string.

```
Calculate_financess(yearly_salary, chargible_income, yearly_multiple, pay_interval, tax_per_interval, currency)
```
Displays yearly and interval-based salary, chargeable income, and tax.

```
main()
```

Orchestrates the program by gathering user inputs, calculating yearly and interval income, and calling the necessary functions to display tax calculations.

## Source
The information used in this program is found in the tax table above, and the calculations were verified against it.
THe tax table was sourced on gov.vc @ [This link](https://finance.gov.vc/finance/index.php/paye-tax-table)
