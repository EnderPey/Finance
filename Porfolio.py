import matplotlib.pyplot as plt
from Yahoo import Stock

class User:
    def __init__(self, name, stocks=[]):
        self.name = name
        self.porfolio = stocks

    def add_stock(self, stock):
        self.porfolio.append(stock)
    def remove_stock(self, stock):
        self.porfolio.remove(stock)
    def __str__(self) -> str:
        out =  self.name + " has "
        for i, stock in enumerate(self.porfolio):
            out += f'{stock}'
            if i != len(self.porfolio) - 1:
                out += ', '
        return out



stonks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']  

ender = User('Ender', [Stock('AAPL', 'history')])
print(ender)
