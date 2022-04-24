check = True
while check:
    try:
        gross_income = int(input("gross income : "))
        number_dependent = int(input("number of dependent : "))
        S_deduction = 10000
        dependent_deduction = 3000
        tax_rate = 0.2
        tax = (gross_income-S_deduction -
               dependent_deduction*number_dependent)*tax_rate
    except:
        continue
    else:
        check = False
if(tax > 0):
    print(tax)
else:
    print("no tax")
