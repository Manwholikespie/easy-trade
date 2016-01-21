#Easy Trade
Easy Trade is a beginner-friendly Command Line Interface (through python) for MarketWatch.com games. It uses [Bradon Wu's](https://github.com/brandonwu) moira library to make trades.  

##Dependencies
There are a few requirements that you must install before using the program.  
1. [Moira](https://github.com/brandonwu/moira)  
2. [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)  

##How to Install Dependencies
If you are on mac, begin by installing homebrew. You can visit their [website](http://brew.sh) for more in-depth help, or type this in to terminal:  
`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  

Once homebrew installs, you need to install python's package manager (pip), and git.  
`brew install pip`  
`brew install git`  

Now, navigate into easy-trade's directory, and fetch moira.  
`git clone https://github.com/brandonwu/moira.git`

Lastly, install and configure beautiful soup.  
`pip install beautifulsoup4`  
`pip install requests`

##Using Easy Trade
While in the easy-trade directory, launch the program with python:  
`python buy.py`

##Side Notes
There is one bug with moira that leads BeautifulSoup complain of its inability to find a default HTML parser... Ignore this.