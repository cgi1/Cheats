[source](https://svn.nmap.org/nmap/zenmap/share/zenmap/config/scan_profile.usp)

[Intense scan]

command = nmap -T4 -A -v
description = An intense, comprehensive scan. The -A option enables OS detection (-O), version detection (-sV), script scanning (-sC), and traceroute (--traceroute). Without root privileges only version detection and script scanning are run. This is considered an intrusive scan.

[Intense scan plus UDP]
command = nmap -sS -sU -T4 -A -v
description = Does OS detection (-O), version detection (-sV), script scanning (-sC), and traceroute (--traceroute) in addition to scanning TCP and UDP ports.

[Intense scan, all TCP ports]
command = nmap -p 1-65535 -T4 -A -v
description = Scans all TCP ports, then does OS detection (-O), version detection (-sV), script scanning (-sC), and traceroute (--traceroute).

[Intense scan, no ping]
command = nmap -T4 -A -v -Pn
description = Does an intense scan without checking to see if targets are up first. This can be useful when a target seems to ignore the usual host discovery probes.

[Ping scan]
command = nmap -sn
description = This scan only finds which targets are up and does not port scan them.

[Quick scan]
command = nmap -T4 -F
description = This scan is faster than a normal scan because it uses the aggressive timing template and scans fewer ports.

[Quick scan plus]
command = nmap -sV -T4 -O -F --version-light
description = A quick scan plus OS and version detection.

[Quick traceroute]
command = nmap -sn --traceroute
description = Traces the paths to targets without doing a full port scan on them.

[Regular scan]
command = nmap
description = A basic port scan with no extra options.

[Slow comprehensive scan]
command = nmap -sS -sU -T4 -A -v -PE -PS80,443 -PA3389 -PP -PU40125 -PY --source-port 53 --script "default or (discovery and safe)"
description = This is a comprehensive, slow scan. Every TCP and UDP port is scanned. OS detection (-O), version detection (-sV), script scanning (-sC), and traceroute (--traceroute) are all enabled. Many probes are sent for host discovery. This is a highly intrusive scan.

