import requests
import json
# URL ="http://127.0.0.1:8000/stu/2"
# r= requests.get(url=URL,timeout=3000)
# data = r.json()


URL2="http://127.0.0.1:8000/stuCreate/"
data={
    "name":"Archana",
    "roll":109 ,
    "city":"Pokhara"
}
json_data = json.dumps(data)
r1 = requests.post(url= URL2, data = json_data)
data1= r1.json()
print(data1)



