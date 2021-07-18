#Mortgage Calculator
#Subprogram1: Monthly Payment
def Monthly_Payment (InterestRate, Principal, Num_MonthlyPayments):
    Monthly_InterestRate = (InterestRate / 100) / 12
    Monthly_Pay = (Monthly_InterestRate * Principal) / (1-(1+Monthly_InterestRate)**(-1 * Num_MonthlyPayments))
    return Monthly_InterestRate
    return Monthly_Pay
#Subprogram2: Debt Schedule
