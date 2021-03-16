In order to drop ping requests (not responding anymore):


```
sudo vim /etc/ufw/before.rules
```

Check for the ping line and change it to DROP (default is ACCEPT):
```
-A ufw-before-input -p icmp --icmp-type echo-request -j DROP
```
Restart firewall

sudo ufw reload
