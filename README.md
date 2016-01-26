#Easy Trade
Easy Trade is a beginner-friendly Command Line Interface (through python) for MarketWatch.com games. It uses [Bradon Wu's](https://github.com/brandonwu) moira library to make trades.  

##Dependencies
There are a few requirements that you must install before using the program.  
1. [Moira](https://github.com/brandonwu/moira)  
2. [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)  

##How to Install Dependencies
###On OS X...
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

###On Linux...
Installation for Linux users is pretty much the same as for OS X, save that apt-get is substituted for home-brew.

###On Windows...
You can visit the [Python Website](https://www.python.org/downloads/release/python-2711/) to download the latest version of the language. This program uses Python 2.7.  
Because you downloaded python straight from their website, pip should already be installed. However, it will need to be upgraded. Run this in CMD/PowerShell:  
`python -m pip install -U pip`  

As for installing git, [git's website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#Installing-on-Windows) has the best information. I will let you choose which path you follow. Once it has been downloaded, navigate into easy-trade's directory, and fetch moira.  
`git clone https://github.com/brandonwu/moira.git`

Lastly, install and configure beautiful soup.  
`pip install beautifulsoup4`  
`pip install requests`


##Using Easy Trade
While in the easy-trade directory, launch the program with python:  
`python buy.py`

##Side Notes
There is one bug with moira that leads BeautifulSoup to complain of its inability to find a default HTML parser... Ignore this.