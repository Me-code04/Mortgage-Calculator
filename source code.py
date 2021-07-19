#Mortgage Calculator
Monthly_InterestRate = (InterestRate / 100) / 12
#Subprogram1: Monthly Payment
def Monthly_Payment (Monthly_InterestRate, Principal, Num_MonthlyPayments):
    Monthly_Pay = (Monthly_InterestRate * Principal) / (1-(1+Monthly_InterestRate)**(-1 * Num_MonthlyPayments))
    return Monthly_Pay
#Subprogram2: Debt Schedule
def Debt_Schedule (Monthly_InterestRate, Principal, Num_MonthlyPayments):
    ##for i in range(Num_MonthlyPayments):
    ##Geometric Series Work
    return None
#Subprogram3: Total Interest
def TotalInterest (Monthly_Pay, Num_MonthlyPayments, Principal):
    Tot_i = (Monthly_Pay*Num_MonthlyPayments) - Principal
    return Tot_i
#Subprogram4: Cumulitive Interest
def CumulitiveInterest (Monthly_Pay, n_payments, Monthly_InterestRate, Principal):
    C_interest = (Principal * Monthly_InterestRate - Monthly_Pay) * ((((1 + Monthly_InterestRate) ** n_payments) - 1)/r) + (Monthly_Pay * n_payments)
    return C_interest
