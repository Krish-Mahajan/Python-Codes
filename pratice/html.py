import urllib.request

wp = urllib.request.urlopen("http://cxp01.designcuisine.com:8080/cxp30/workerHomePage.action?CatererID=DESIGN&SessionID=-142986637&PlsqlUrl=http://cxp01.designcuisine.com/pls/")
print(type(wp))
pw = wp.read()
print(pw)