import urllib

optionsUrl = "http://finance.yahoo.com/q/op?s=AAPL+Options"

optionsPage = urllib.urlopen(optionsUrl)
