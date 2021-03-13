from django.shortcuts import render
import redis
from urllib.request import Request
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
url="http://www.bseindia.com/download/BhavCopy/Equity/EQ080321_CSV.ZIP"
req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
resp = urlopen(req)
redis_host = "localhost"
redis_port = 6379
redis_password = ""
zipfile = ZipFile(BytesIO(resp.read()))
from django import template
register = template.Library()

def bhav_copy(request):
    alldata= []
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    keys = r.keys('*')
    for each in keys:
        msg = r.get(each)
        alldata.append(msg)
    params = {'allProds':alldata}
    print(alldata)
    return render(request, 'stocks.html', params)