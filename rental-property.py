#def __init__(self, n):
#if type(n) != int: 
# raise TypeError('Please input an integer.')
#, cost_of_home, mthly_income, taxes_topay,insurance_topay,utilities_topay,hoa_topay,vacancy_saved,repairs_saved,property_management,mortage_topay,Down_payment,Closing_cost,rehab_budget,misc_other
#self.cost_of_home=int(input("what is the cost of the home?"))
#    self.mthly_income= int(input(" What would be your monthly income from this property?"))
#   self.taxes_topay= int(input("how much taxes would you pay for this property? \n the average property tax rate is 1.17%.  "))
#  self.insurance_topay= int(input(" Annual home insurance: \n search for average annual home insurance in your state if unknown" ))
# self.utilities_topay= int(input (" Are utilities being paid by the tenant or you? \ if its you please enter total utility expense \n if tenant please enter 0"))
#self.hoa_topay= int(input(" Do you have an HOA payment? \n if yes enter amount, otherwise enter 0"))
#self.vacancy_saved= int(input(" What you would save for vacancy(monthly):  \n We recommend you save $100 monthly for possibe vacancy!  "))
#self.repairs_saved = int(input("What you would save for repairs( monthly):  \n we recommend 120 monthly for possible repairs"))
#self.property_management= int(input("what do you pay for property management? if none enter 0"))
#self.mortage_topay= int(input("what is your monthly mortage payment? if none enter 0"))
#self.Down_payment= int(input("How much money did you put as your down payment?"))
#self.Closing_cost= int(input("How much were the closing cost")
#self.rehab_budget= int(input('did you make cosmetic changes? if yes how much did you spend?')
#self.misc_other= int(input(' other investments and cash used for the property?'))
class Income():


    def __init__(self, rentalIncome, extraIncome= 0): 
        self.rentalI = int(rentalI)
        self.extraI = int(extraI)

    def calcIncome(self): 
        self.income = self.rentalIncome + self.extraIncome
        return self.income

class Expenses():

    def __init__(self, tax,insurance,utilities,HOA,yardCare,vacancy,repairs,capex,management,mortgage): #takes in all the varaibles need to to calculate expenses
        self.tax = int(tax)
        self.insurance = int(insurance)
        self.utilities = int(utilities)
        self.HOA = int(HOA)
        self.yardCare = int(yardCare)
        self.vacancy = int(vacancy)
        self.repairs = int(repairs)
        self.capex = int(capex)
        self.management = int(management)
        self.mortgage = int(mortgage)


    def calcExpenses(self): #calculates total expenses
        self.expenses = self.tax + self.insurance + self.utilities + self.HOA + self.yardCare + self.vacancy + self.repairs + self.capex + self.management + self.mortgage
        return self.expenses 

class ROI():

    def __init__(self,downPay,closingCost): #takes in all the varaibles you will need to calculate the retrun on investment
        self.downpay = int(downPay)
        self.closingCost = int(closingCost)
       

    def calcCashFlow(self): #calculates cash flow
        self.cashFlow = self.income - self.expenses
        return self.cashFlow    

    def totalInvestment(self): #calculates money spent on property 
        self.totalDown = self.downpay + self.closingCost 
        return self.totalDown
    
    def annualCashFlow(self): #calcluates yearly cashflow from property
        self.annualCash = self.cashFlow *12
        return self.annualCash

    def totalROI(self): #calculates RIO
        self.totalROI = self.annualCash / self.totalDown
        return '{0:.2%}'.format(self.totalROI)

class Proptery(Income,Expenses,ROI):

    def __init__(self,cost,cost1,type,rentalI,extraI,tax,insurance,utilities,HOA,yardCare,vacancy,repairs,capex,management,mortgage,downPay,closingCost): # takes in all the information about the rental property
        Income.__init__(self, rentalI, extraI)
        Expenses.__init__(self, tax,insurance,utilities,HOA,yardCare,vacancy,repairs,capex,management,mortgage)
        ROI.__init__(self,downPay,closingCost)
        self.cost = int(cost)
        self.cost1= int(cost)
        self.type = type

    def propInfo(self):
        print("____________________________________")
        print(f"The {self.type} you are looking to buy costs ${self.cost}")
        print(f"Your total rental income is ${self.calcIncome()}")
        print(f"Your total expenses are ${self.calcExpenses()}")
        print(f"Your total cash flow is ${self.calcCashFlow()}")
        print(f"Your total investment is ${self.totalInvestment()}")
        print(f"Your total anual cashflow is ${self.annualCashFlow()}")
        print(f"Your total anual ROI is {self.totalROI()}")


class Main(): 

    def check(var): #checks if the input is an integer
        try:
            if isinstance(int(var),int):
                return False
        except ValueError:
            print("Invalid input please try input a integer!")
            return True

    def run():
        
        rentalType = input("What kind of property are you purchasing/have purchased? (ex: apartment, duplex, house) ").strip()
        a = True
        while a == True:
            cost = input("How much is the property you are trying to buy? (no comas please) ").strip()
            a = Main.check(cost)
        a = True
        while a == True:
            cost1 = input("How much did you put as a downpayment? (If you payed full please input here) ").strip()
            a = Main.check(cost1)
        a = True
            
        while a == True:
            rentalIncome = input("How much rent will you charge? ").strip()
            a = Main.check(rentalIncome)
        a = True
        while a == True:
            extraIncome = input("Do you make any extra income from this property? ").strip()
            a = Main.check(extraIncome)
        a = True
        while a == True:
            tax = input("How much will you be paying in propety taxes? ( Enter what one of your payments would be.) ").strip()
            a = Main.check(tax)
        a = True
        while a == True:
            insurance = input("How much will you be paying in insurance?( Enter what one of your payments would be.)").strip()
            a = Main.check(insurance)
        a = True
        while a == True:
            utilities = input("How much will you be paying for utilities? (if none enter 0) ").strip()
            a = Main.check(utilities)
        a = True
        while a == True:
            HOA = input("How much will you have to pay to the HOA's? (if none enter 0) ").strip()
            a = Main.check(HOA)
        a = True
        while a == True:
            yardCare = input("How much will you pay for in yard care?(if none enter 0) ").strip()
            a = Main.check(yardCare)
        a = True
        while a == True:
            vacancy = input("How much will you set aside for vacancy? (we recommend atleast $50 monthly) ").strip()
            a = Main.check(vacancy)
        a = True
        while a == True:
            repairs = input("How much will you set aside for repairs? (we recommend 5% of the rental income) ").strip()
            a = Main.check(repairs)
        a = True
        while a == True:
            capex = input("How much will you set aside for capital expenses? ").strip()
            a = Main.check(capex)
        a = True
        while a == True:
            management = input("How much are you going to pay for property management? ").strip()
            a = Main.check(management)
        a = True

       
        while True:
            payInFull = input("Will you be paying in full 'yes' or 'no'? ").lower().strip()
            if payInFull == 'no':
                while a == True:
                    mortgage = input("How much will your mortgage payment be? ").strip()
                    a = Main.check(mortgage)
                a = True
                
                break
            elif payInFull == 'yes':
                mortgage = 0
                downPay = cost1
                break
            else:
                print("Invalid input please enter 'yes' or 'no'" )   

        while a == True:
            closingCost = input("How much will the closing cost be? ").strip()
            a = Main.check(closingCost)
        a = True
     

        rental = Proptery(cost1,cost,rentalType,rentalIncome,extraIncome,tax,insurance,utilities,HOA,yardCare,vacancy,repairs,capex,management,mortgage,closingCost)

        
        rental.propInfo()
        

Main.run()