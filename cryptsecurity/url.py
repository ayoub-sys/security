import urllib.request as req
urlresponse= req.urlopen("https://google.com")
print(urlresponse.info())
print(urlresponse.info()["Expires"])