import re
import json
import urllib
import urllib.request
import urllib.error
from urllib.request import urlopen


url = urllib.request.urlopen('http://ipinfo.io/json')
data = json.load(url)

IP=data['ip']
org=data['org']
city = data['city']
region=data['region']
country=data['country']


print ('Your IP detail\n ')
print ('IP : {4} \nCity : {3} \nRegion : {1} \nCountry : {2} \nOrg : {0}'.format(org,region,country,city,IP))
