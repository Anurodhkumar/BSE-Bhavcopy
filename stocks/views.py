from django.shortcuts import render
import redis
from urllib.request import Request
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
url="http://www.bseindia.com/download/BhavCopy/Equity/EQ080321_CSV.ZIP"
req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
resp = urlopen(req)
redis_host = "redis-15364.c92.us-east-1-3.ec2.cloud.redislabs.com"
redis_port = 15364
redis_password = "iQuSqk1AO4S4M6JW4gXB45SZzQqL4Del"
zipfile = ZipFile(BytesIO(resp.read()))
from django import template
register = template.Library()

def bhav_copy(request):
    alldata= []
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    keys = r.keys('*')
    msg = r.get('ids2')
    params = {'allProds':alldata}
    return render(request, 'stocks.html', params)
