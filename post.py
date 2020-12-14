import requests
import time
import base64

t1 = time.time()
s = requests
with open('./me.jpg', 'rb') as f:
    imgbase64_1 = base64.b64encode(f.read())
with open('./1.jpg', 'rb') as f:
    imgbase64_2 = base64.b64encode(f.read())
data={"imgdata1":imgbase64_1,"imgname1":'me.jpg',"imgdata2":imgbase64_2,"imgname2":'./1.jpg',"alpha":0.85,"mat_multiple":0.9}
r = s.post("http://127.0.0.1:8881/facemerge", data)

print(r)
print(r.text)
print('time cost:', time.time() - t1)
