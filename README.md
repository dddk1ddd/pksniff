# psniff
PktMon Pyhon Script for Windows 10
with basic (untested) examples for bash and powerscript

You will have to add your own filters. Run as administrator.

See documentation for pktmon using pktmon help, pktmon filter help.

Example filter:

pktmon filter add -p 53 | Add port 53 (TCP and UDP, IPv4 and IPv6)

pktmon filter remove | Remove all filters and monitor all traffic
