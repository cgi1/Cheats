
# Show different `iommu_groups`.

```
root@pve:~# for a in /sys/kernel/iommu_groups/*; do find $a -type l; done | sort --version-sort
```


# Check different IDs:
To check which devices are included in which iommu_group, we resolve it from lspci:
```
lspci -vv > lspci-vv.txt
```

replace 23:00 with the device id (last part behind 0000:)

```
cat lspci-vv.txt | grep 23:00
```

[Source 1](https://www.heiko-sieger.info/iommu-groups-what-you-need-to-consider/)
[Source 2]()

> IOMMU – or input–output memory management unit – is a memory management unit (MMU) that connects a direct-memory-access–capable (DMA-capable) I/O bus to the main memory. The IOMMU maps a device-visible virtual address ( I/O virtual address or IOVA) to a physical memory address. In other words, it translates the IOVA into a real physical address.
