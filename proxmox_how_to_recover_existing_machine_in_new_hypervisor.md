[Link](https://manjaro.site/how-to-create-a-new-virtual-machine-from-an-existing-disk-image-in-proxmox/)

- Basically create a fresh VM and adapt the `nano /etc/pve/qemu-server/100.conf` file, where `100` is the id of the machine.
- Exchange scsi0 / scsi1 or (for Windows) ide to the target disks.
- Adjust memory, cpu and BIOS
- Make sure hardware changes are seen by GUI
- Start machine.
