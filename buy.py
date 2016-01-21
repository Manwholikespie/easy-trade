#from googlefinance import getQuotes
from bs4 import BeautifulSoup
from moira import moira
import time
import json
import re

def searchStock(tickerSymbol):
    searchData = str(moira.stock_search(token, game, tickerSymbol))
    re1='.*?'	# Non-greedy match on filler
    re2='\\\'.*?\\\''	# Uninteresting: strng
    re3='.*?'	# Non-greedy match on filler
    re4='\\\'.*?\\\''	# Uninteresting: strng
    re5='.*?'	# Non-greedy match on filler
    re6='(\\\'.*?\\\')'	# Single Quote String 1

    rg = re.compile(re1+re2+re3+re4+re5+re6,re.IGNORECASE|re.DOTALL)
    m = rg.search(searchData)
    if m:
        strng1=m.group(1)
        return (strng1).replace("'","")

def buyStock(token, game, action, tickerSymbol, amt, times):
    print("Buying...")
    for x in xrange(0,times):
        moira.order(token, game, action, tickerSymbol, amt)
    print("Transaction complete.")

### MAIN FUNCTION ###

# SET UP MOIRA
print("Welcome to Manwholikespie's MarketWatch CLI interface.\n\n")
username = raw_input("Please enter your MarketWatch email.\n > ")
password = raw_input("Please enter your MarketWatch password. (Warning, not hidden)\n > ")
print("Logging in...")

token = moira.get_token(username, password)
game = raw_input("Please enter your game id. Ex: meisenheimer\n > ")

print("I'm guessing you would like to buy.")
inputTicker = raw_input("Please enter the ticker symbol. Ex: AAPL\n > ")

print("Searching for stock's security id.")
symbol = searchStock(inputTicker)
amount = raw_input("How many would you like to buy? (Beware of volume restrictions)\n > ")
times = int(raw_input("How many times should this repeat?\n If only once, type 1.\n > "))

buyStock(token, game, 'Buy', symbol, amount, times)
