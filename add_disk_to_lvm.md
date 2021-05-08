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

(add all the blocks by pressing ENTER)

5. Now create the partition

Once again, we find the partition where we want to create a filesystem on using `fdisk -l`. Here it is `/dev/sdb1`

```
mkfs -t ext4 /dev/sdb1
```

6. Create & Mount the newly added disk


```
mkdir -p /mnt/large/
mount -t auto /dev/sdb1 /mnt/large/
```

7. Check and be happy


```
df -h
```

(find your newly created file system under your mounting point)
