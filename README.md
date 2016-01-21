#Easy Trade
Easy Trade is a beginner-friendly Command Line Interface (through python) for MarketWatch.com games. It uses Bradon Wu's moira library to make trades.  

##Dependencies
There are a few requirements that you must install before using the program.  
1. Moira  
2. Beautiful Soup  

##How to Install Dependencies
If you are on mac, begin by installing homebrew. You can visit their website at brew.sh, or type this in to terminal:
`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  

Once homebrew installs, go ahead and navigate into easy-trade's directory, and fetch moira.  
`git clone https://github.com/brandonwu/moira.git`

Now, you need beautiful soup.  
`pip install beautifulsoup4`

##Using Easy Trade
While in the easy-trade directory, launch the program with python:  
`python buy.py`