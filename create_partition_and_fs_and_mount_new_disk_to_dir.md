How to add another disk (e.g. from Proxmox or ESX) to an existing LVM (or mount it to a data folder)




1. Show the physical disks

```
fdisk -l
```

2. Get into partitioning

```
fdisk /dev/sdb
```

3. Delete existing partitions on disk


```
d
```

4. Create new partition

```
n
```

5. Save made changes using `w`

(add all the blocks by pressing ENTER)

----

1. Now create the file system

Once again, we find the partition where we want to create a filesystem on using `fdisk -l`. Here it is `/dev/sdb1`

```
mkfs -t ext4 /dev/sdb1
```

2. Create & Mount the newly added disk


```
mkdir -p /mnt/large/
chown g:g /mnt/large/
mount -t auto /dev/sdb1 /mnt/large/
```

7. Check and be happy


```
df -h
```

(find your newly created file system under your mounting point)

8. Add on system boot

[Find out the UUID](https://askubuntu.com/a/303499/864617):

```
sudo blkid
```

Enter it like this (replace the UUID and the mount location) to `/etc/fstab`
```
UUID=1187991b-c0f8-4086-bcdc-fe50d949bf67    /mnt/large   auto    rw,user,auto    0    0
```
