# Out-Of-Memory Killer

Typical failure:

```
Out of Memory: Killed process 12345 (postgres).
```

Reason: OOM kills most consuming / dempanding process.


> 2: Setting the variable to 2 means that kernel is not supposed to overcommit memory greater than the overcommit_ratio. This overcommit_ratio is another kernel setting where you specify the percentage of memory kernel can overcommit. If there is no space for overcommit, the memory allocation function fails and overcommit is denied. This is the safest option and recommended value for PostgreSQL.   


[Quote](https://www.percona.com/blog/2019/08/02/out-of-memory-killer-or-savior/)

```
echo 2 > /proc/sys/vm/panic_on_oom
```

```
sudo -s sysctl -w vm.oom-kill = 2
```

```
```


