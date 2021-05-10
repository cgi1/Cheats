Author: Christoph Giese


[Following this tut](https://www.ryadel.com/en/resize-extend-disk-partition-unallocated-disk-space-linux-centos-rhel-ubuntu-debian/)


1. Check for available space



```
sudo apt-get install cfdisk
```


```
cfdisk
```

(Note down the partition we want to extend)

2. Note down the start/end of the partitions like this:




3. Alter the Partition Table

```
sudo fdisk /dev/sda
```

Print partition table:

```
p
```

Output:

```
Disk /dev/sda: 96 GiB, 103079215104 bytes, 201326592 sectors
Disk model: QEMU HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x948370d1

Device     Boot   Start      End  Sectors  Size Id Type
/dev/sda1  *       2048  1050623  1048576  512M  b W95 FAT32
/dev/sda2       1052670 67106815 66054146 31.5G  5 Extended
/dev/sda5       1052672 67106815 66054144 31.5G 83 Linux
```

Now delete the partition (MAKE SURE TO HAVE A SNAPSHOT!) --> `2` for `sda2`:

```
d
2
```

Using `p`, we can see that the partitions are empty:

```
Command (m for help): p
Disk /dev/sda: 96 GiB, 103079215104 bytes, 201326592 sectors
Disk model: QEMU HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x948370d1

Device     Boot   Start      End  Sectors  Size Id Type
/dev/sda1  *       2048  1050623  1048576  512M  b W95 FAT32
```

Pretty scary, right? So now we create a new partition, with **the same settings**, but different end:

```
n
```
For partition type choise `p` if you deleted a `primary` partition and `e` if you `deleted` an extended partition.


```
A
```


```
A
```


```
A
```


```
A
```

