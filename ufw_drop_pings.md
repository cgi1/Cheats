# Prep

Make sure ufw is running

```
sudo ufw status
```

Enable it if not (MAKE SURE THAT YOU HAVE A KVM or ANOTHER DIRECT ACCESS IF SSH BREAKS!)

```
sudo ufw enable
```


In order to drop ping requests (not responding anymore):


```
sudo vim /etc/ufw/before.rules
```

Check for the ping line and change it to DROP (default is ACCEPT):
```
-A ufw-before-input -p icmp --icmp-type echo-request -j DROP
```
Restart firewall

```
sudo ufw reload
```
