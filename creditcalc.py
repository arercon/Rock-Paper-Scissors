import math, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Type 'annuity' for annuitly payment or 'diff'")
parser.add_argument("--principal", type=int, help="principal amount")
parser.add_argument("--periods", type=int, help="Months you have to pay")
parser.add_argument("--interest", type=float, help="Interest in float number(e.g. 4.5)")
parser.add_argument('--payment', type=float, help="Monthly payment")
args = parser.parse_args()

if len(sys.argv) < 5:
    print("Incorrect parameters")
    sys.exit()
    
for x in range(1, len(sys.argv)+1):
    if x is not None:
        if x < 0:
            print("Incorrect parameters")
            sys.exit()  

principal = args.principal
months = args.periods
payment = args.payment
if args.interest == None:
    print("Incorrect parameters")
    sys.exit()
i = args.interest / 1200
 
 
if args.type == 'diff':
    overpayment = 0
    for m in range(1, months+1):
        dm = math.ceil((principal / months)+i*(principal-(principal*(m-1))/months))
        print(f"Month {m}: payment is {dm}")
        overpayment += dm
    print(f"Overpayment = {overpayment-principal}")

elif args.type == 'annuity':
    if months == None: # number of months until principal is paid calculation
        months = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
        years = int(months / 12)
        overpayment = principal - (months*payment)
        months = months % 12
        if years == 0:
            print("It will take {} month{} to repay this loan!\nOverpayment = {}".format(months,
             '' if months == 1 else 's', abs(overpayment)))
        elif months == 0:
            print("It will take {} year{} to repay this loan!\nOverpayment = {}".format(years,
             '' if years == 1 else 's', abs(overpayment)))
        else:
            print("It will take {} year{} and {} month{} to repay this loan!\nOverpayment = {}".format(years,
                '' if years == 1 else 's', months, '' if months == 1 else 's', abs(overpayment)))       
    elif payment == None: # monthly payment amount calculation
        payment = math.ceil(principal * ((i * math.pow(1 + i, months)) / (math.pow(1 + i, months) - 1)))
        last_pay = principal-(months-1)*payment
        overpayment = abs(principal - (months*payment) - last_pay)
        print(f"Your monthly payment = {payment}\nOverpayment = {overpayment}")
    elif principal == None: # principal payment calculation
        principal = payment / ((i * math.pow(1 + i, months)) / (math.pow(1 + i, months) - 1))
        overpayment = principal - (months * payment)
        print(f"Your loan principal = {round(principal,2)}\nOverpayment = ")
else:
    print("Incorrect parameters")
