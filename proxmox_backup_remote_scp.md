### Mount remote dir

To directly push the backup to remote host, mount remote dir ([eg using sshfs](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh))

```
apt-get install sshfs
mkdir /mnt/pve3 # <--replace "pve3" whatever you prefer
sshfs -o allow_other,default_permissions root@192.168.178.224:/mnt/pve/hugetempdir/ /mnt/pve3
```

### Do backup to mount point

```
# replace
# 501 = vmid
# pve2 = Name source proxmox host

vzdump 501 --node pve2 --mode snapshot --remove 0 --compress zstd --dumpdir /mnt/pve3/dump/
```


### Restore backup on target server

1. Search for the disk target storage using `cat /etc/pve/storage.cfg`
2. replace in command
3. Fire

```
qmrestore vzdump-qemu-501-2021_11_08-12_59_34.vma.zst 501 --storage local-lvm
```


[Credits](https://cyberpersons.com/2016/09/13/backup-transfer-proxmox-vm-another-proxmox-node/#Create_backup_from_command_line)
