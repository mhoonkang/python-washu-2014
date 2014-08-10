import random

# make class Portfolio
class Portfolio():
  def __init__(self, cash=0, stock={}, mf={}):
    self.cash = float(cash)
    self.stock = stock # the names of the stock will be keys, the amount of the stock will be the values.
    self.mf = mf # the names of the mutual fund will be keys, the amount of the mutual fund will be the values.
    self.stock_price = {} # the names of the stock will be keys, the price of the stock will be the values.
    self.hist = [] # transcation history will be store here by time order
	 
  def __str__(self):
    portfolio_print = [] # this will be the list for printing
    str_cash = "${0:.2f}".format(self.cash) # the amount of cash to two decimal places with dolar sign.
    cash_print = "{:>14} {:>14}" .format("cash: ", str_cash) # this will print like " cash:    $000.00" 
    portfolio_print.append(cash_print) # add  cash print to the list
    stock_amount = self.stock.values() # stock amount
    stock_name = self.stock.keys() # stock name
    for i in range(len(self.stock)): 
      if i == 0: # this is for the first line of the stock 
	stock_first_line = "{:>14} {:>14} {:<10}" .format("stock: ", stock_amount[i], stock_name[i]) # this will print the first line of the stock like " stock:   00"
        portfolio_print.append(stock_first_line) # add stock print to the list
      else: # this is for the rest lines of the stock
	stock_rest_line = "{:>14} {:>14} {:<10}" .format("      ", stock_amount[i], stock_name[i]) #this will print the rest lines of the stock like "          00"
        portfolio_print.append(stock_rest_line) # add stock print to the list
    mf_amount = self.mf.values() # mutual fund amount 
    mf_name = self.mf.keys() # mutual fund name
    for i in range(len(self.mf)): # the rest of the codes follows the same logic of the stock print
      if i == 0: 
	mf_first_line = "{:>14} {:>14} {:<10}" .format("mutual funds: ", "{0:.2f}".format(mf_amount[i]), mf_name[i])
        portfolio_print.append(mf_first_line)
      else:
	mf_rest_line = "{:>14} {:>14} {:<10}" .format("             ", "{0:.2f}".format(mf_amount[i]), mf_name[i])
        portfolio_print.append(mf_rest_line) 
    return "\n".join(portfolio_print) # return the list line by line

  def addCash(self, amount=0):
    amount = float(amount)
    self.cash += amount
    self.hist.append(["add cash", "+${0:.2f}".format(amount)])

  def buyStock(self, amount, object): 
    if object.name in self.stock.keys(): # if you already have the stock, then the amount you input will be added to the key for the stock in the list
      self.stock[object.name] += amount 
    else: self.stock[object.name] = amount # if you do not have the stock, then new key will be created and the amount you input will be stored there.
    self.stock_price[object.name] = object.price # store the stock price
    self.cash -= object.price*amount # subtract the amount of cahs you spend for buying the stock
    self.hist.append(["buy {0} {1} stock(s)".format(amount, object.name), "-${0:.2f}".format(object.price*amount)]) # store the transaction history list to the history list

  def buyMutualFund(self, amount, object):
    amount = float(amount)
    if object.name in self.mf.keys(): # if you already have the mutual fund, then the amount you input will be added to the key for the stock in the list
      self.mf[object.name] += amount
    else: self.mf[object.name] = amount # if you do not have the mutual fund, then new key will be created and the amount you input will be stored there.
    self.cash -= object.price*amount # subtract the amount of cahs you spend for buying the mutual fund
    self.hist.append(["buy {0} {1} mutual funds".format(amount, object.name), "-${0:.2f}".format(amount)]) # store the transaction history list to the history list
  
  def sellMutualFund(self, name, amount):
    amount = float(amount)
    if name not in self.mf.keys(): # if you don't have the mutual fund you input, then print the following message.
      print "There is not {0} in your portfolio!".format(name)
    else: # if you have the mutual faund you input,
      income = amount*random.uniform(0.9, 1.2)  # the income you get will be determined
      self.cash += income # then it will be added to the cash you have
      if round(self.mf[name],2) == amount: #if you sell all the mutual fund you have
        del self.mf[name] # delete the mutual fund from you portfolio 
      else:
        self.mf[name] -= amount # if you do not sell all, then subtract the amount you sell from the existing amount of the mutual fund you have
      self.hist.append(["sell {0} {1} mutual funds".format(amount, name), "+${0:.2f}".format(income)])# store the transaction history.

  def sellStock(self, name, amount):
    if name not in self.stock.keys(): # if you don't have the stock you input, then print the following message.
      print "There is not {0} in your portfolio!" .format(name)
    else: # if you have the stock you input,
      income = amount*random.uniform(0.5, 1.5)*self.stock_price[name] # the income you get will be determined
      self.cash += income # then it will be added to the cash you have
      if self.stock[name] == amount: #if you sell all the stock you have
        del self.stock[name] # delete the mutual fund from you portfolio 
      else:
        self.stock[name] -= amount # if you do not sell all, then subtract the amount you sell from the existing amount of the stock you have
      self.hist.append(["sell {0} {1} stocks".format(amount, name), "+${0:.2f}".format(income)]) # store the transaction history.

  def withdrawCash(self, amount):
    amount = float(amount)
    self.cash -= amount # subtract the cahs you withdraw from the amount of the cash you have
    self.hist.append(["withdraw cash", "-${0:.2f}".format(amount)]) # store the transaction history.

# I print the history in the much easily recognizable way.
# print the transaction history list will be simply done by 'print self.hist'.
  def history(self):
    for line in self.hist:
      print "{:<28} {:>14}".format(*line) # print all the transaction history list line by line
    print "{:<28} {:>14}" .format("----------------------", "-------------")
    print "{:<28} {:>14}" .format("total", "${0:.2f}".format(self.cash))

# make class Stock
class Stock():
  def __init__(self, price, name):
    self.price = price # the price of the stock
    self.name = name # the name of the stock

  def __str__(self):
    outcome = "price: ${0}, symbol: {1}" .format(self.price, self.name)
    return outcome

# make class MutualFund
class MutualFund():
  def __init__(self, name):
    self.name = name # the name of the mutual fund
    self.price = 1 # the price of the mutual fund = 1

  def __str__(self):
    outcome = "price: ${0}, symbol: {1}" .format(self.price, self.name)
    return outcome

# extending the program by including Bond

# make subclass of portfolio, Portfolio_2
# this subclass inherited from Portfolio
class Portfolio_2(Portfolio):
  def __init__(self, bond={}):
    Portfolio.__init__(self, cash=0, stock={}, mf={})
    self.bond = bond # this is what newly added to the subclass. The keys are the bond name and the values are the amount of the bond you have.


  def __str__(self):
    portfolio2_print = []
    bond_amount = self.bond.values() # the amount of bond
    bond_name = self.bond.keys() # the name of the bond
    for i in range(len(self.bond)):
      if i == 0: # this is for the first line of the bond 
	bond_first_line = "{:>14} {:>14} {:<10}" .format("bonds: ", "{0:.2f}".format(bond_amount[i]), bond_name[i]) # this will print the first line of the bond like " bond:   00"
        portfolio2_print.append(bond_first_line) # add stock print to the list
      else:
	bond_rest_line = "{:>14} {:>14} {:<10}" .format("             ", "{0:.2f}".format(bond_amount[i]), bond_name[i]) #this will print the rest lines of the stock like "          00"
        portfolio2_print.append(bond_rest_line) # add stock print to the list
    return "{0}\n{1}".format (Portfolio.__str__(self), "\n".join(portfolio2_print)) # print bond information after what inherited from the class Portfolio. 

# making add and buy function for bonds will be easy but I skipped it because there is no information about how to deal with it.
# Let's see what happen :)
	
portfolio = Portfolio()
portfolio.addCash(300.50)
a = Stock(20, "HFH")
portfolio.buyStock(5, a)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print portfolio
portfolio.history()
portfolio.withdrawCash(50)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
print portfolio
portfolio.sellMutualFund("BRT", 7.3)
portfolio.sellStock("HFH", 4)
print portfolio
portfolio.history()

portfolio2 = Portfolio_2({"BBB": 60, "ABC": 50})
portfolio2.addCash(300.50)
a = Stock(20, "HFH")
portfolio2.buyStock(5, a)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio2.buyMutualFund(10.3, mf1)
portfolio2.buyMutualFund(2, mf2)
print portfolio2
portfolio2.history()
