#Four square ROI method Bigger Pockets
#Based on 200k duplex
#First square is INCOME
    #Rental income = 2000$/month
    #Laundry income =0
    #storage income =0
    #misc =0
    #Total monthly income = 2000$


#Second Square is EXPENSES
    #Taxes = $150/mo
    #Insurance = $100/mo
    #Utilities = $0
        #Electric,water,sewer,garbage,gas
    #HOA fees = $0
    #Lawn care = $0
    #Vacancy = $100/mo
    #Repairs = $100/mo
    #Capital expendacures, saving for big things = $100/mo
    #Property Management = $200/mo
    #Morgage = $860/mo
    #Total expenses: $1610/mo

#Box 3 is CASH FLOW = INCOME - EXPENSES
    #Income = $2000
    #Expenses = $1610
    #Cashflow = $390

#Box 4 is cash on cash ROI
    #Down Payment = $40k
    #Closing Costs = $3000
    #Rehab Budget = $7000
    #Misc = $0
    #Total Investment = $50k
    #Annual Cash flow = $4680
    #Cash on Cash = Annual/ total investment * 100
    #Cash on Cash ROI = 9.36%

def fillDict(theDict):
    printDict(theDict)
    response = input("Does everything look correct? (Yes/No)")
    while response.lower() != 'yes':
        for keys in theDict.keys():
            try:
                theDict[keys] = int(input(f'What is your {keys} ? (Round up to the nearest dollar)'))
            except:
                print("You'll have to try again")
        
        printDict(theDict)
        response = input("Does everything look correct? (Yes/No)")
        
def printDict(theDict):
    print("Every Value is per month: ")
    for keys, values in theDict.items():
        print(f'{keys} = ${values}')

def returnTotal(theDict):
    total =0
    for values in theDict.values():
        total+=values
    return total

def fillOne(theDict):
    printDict(theDict)
    response = input("Which Value would you like to change? ('Quit' To Quit)")
    while response.lower()!= "quit":
        if response in theDict.keys():
            theDict[response]= int(input(f'What is your {response}?\n'))
        else:
            print("Something went wrong make sure the value is spelt correctly")
        printDict(theDict)
        response = input("Which Value would you like to change? ('Quit' To Quit)")

def options(theDict):
    result = input("Would you like to:\n(1) Fill out the entire list\n(2) Change an individual Value\n(3) Print out your values\n(4) Quit")
    while result != "4":
        
        if result == "1":
            fillDict(theDict)
        elif result == "2":
            fillOne(theDict)
        elif result == "3":
            printDict(theDict)
        else:
            print("Please try again:\n")
        result = input("Would you like to:\n(1) Fill out the entire list\n(2) Change an individual Value\n(3) Print out your values\n(4) Quit")
    
def printMinList(theDict):
    print("Every Value is per month: ")
    for keys, values in theDict.items():
        if values != 0:
            print(f'{keys} = ${values}')   
    
income = {
    "Rental Income": 0,
    "Laundry Income": 0,
    "Storage Income":0,
    "Misc Income": 0,

}

expenses = {
    "Morgage": 0,
    "Taxes": 0,
    "Insurance": 0,
    "Utilites": 0,
    "HOA fees": 0,
    "Lawn Care": 0,
    "Vacancy": 0,
    "Repairs": 0,
    "Capital Expendacures": 0,
    "Property Management": 0,
    "Misc Expenses": 0,
}

invested = {
    "Down Payment": 0,
    "Closing Costs": 0,
    "Rehab Budget": 0,
    "Misc Invested": 0,
}


purchase_price =0
income_total=0
expenses_total = 0
investment_total =0


purchase_price= int(input("What was the purchase price of the property? (Round up to the nearest dollar)"))

while True:
    result= input("Which list would you like to fill out?\n(1) Income\n(2) Expenses\n(3) Invested\n(4) See your Results")
    if result == "1":
        options(income)
    elif result == "2":
        options(expenses)
    elif result == "3":
        options(invested)
    elif result =="4":
        ask = input("Did you fill out every List? (Yes/No)")
        if ask.lower() =="yes":
            break
        else:
            print("Go back and fill it out for accurate results")


income_total= returnTotal(income)
expenses_total= returnTotal(expenses)
investment_total = returnTotal(invested)

cash_flow = income_total - expenses_total
annual_cash = cash_flow * 12
print(f'On the ${purchase_price} property here are your results:\n')
print(f'Total Income: ${income_total}')
print(f'Total Expenses: ${expenses_total}')
print(f'Total Invested: ${investment_total}')
print(f'Annual Cash Flow: ${annual_cash}')
print(f'Cash on Cash ROI: {(annual_cash/investment_total)*100}%')

