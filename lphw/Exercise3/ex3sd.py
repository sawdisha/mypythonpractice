print("Calculationg coumpund interest...")
p = 125000 #Principal amount
t = 5.25 #Loan time period in years
r = 16 #Rate of interest

#Equation to calculate compound interest
ci = p*(pow((1+r/100),t)) #pow() function returns the value of (1+r/100) to the power of t

print("Compound interest on the loan is:",ci)
