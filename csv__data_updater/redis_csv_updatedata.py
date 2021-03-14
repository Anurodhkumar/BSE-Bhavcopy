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
def csv_data(request):
    r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    for key in r.scan_iter("prefix:*"):
        r.delete(key)
    count=1
    newdata = []
    for line in zipfile.open(zipfile.namelist()[0]).readlines():
        count += 1
        if count > 3:
            alldata = line.decode('utf-8').split(',')
            data = [alldata[0],alldata[1],alldata[4],alldata[5],alldata[6],alldata[7]]
            newdata.append(data)
    r.set("ids2", str(newdata))
   
    
   
