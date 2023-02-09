import subprocess


def _main():
    print("\n *** WARNING! This script will remove" +
          "\n *** any PktMon filters you have enabled." +
          "\n *** Exit now to avoid losing filters.\n")
    try:
        while True:
            command = input("Enter command:\n\n dns\n tcp\n dhcp\n ftp\n telnet\n icmp\n smb\n device\n list\n lookup\n exit\n\n? ")

            if command == "lookup":
                addy = input("\nAddress? ")
                subprocess.run(["nslookup", addy])
            if command == "dhcp":
                subprocess.run(["pktmon", "filter", "remove"])
                subprocess.run(["pktmon", "filter", "add", "DhcpTraffic", "-t", "UDP", "-p", "67"])
                subprocess.run(["pktmon", "filter", "add", "DhcpTraffic", "-t", "UDP", "-p", "68"])
                print("Monitoring...\n\n")
                try:
                    subprocess.run(["pktmon", "start", "-c", "-m", "real-time"])
                except KeyboardInterrupt:
                    pass
            if command == "smb":
                    subprocess.run(["pktmon", "filter", "remove"])
                    subprocess.run(["pktmon", "filter", "add", "SMB", "-t", "TCP", "SYN", "-p", "445"])
                    print("Monitoring...\n\n")
                    try:
                        subprocess.run(["pktmon", "start", "-c", "-m", "real-time"])
                    except KeyboardInterrupt:
                        pass
            if command == "icmp":
                subprocess.run(["pktmon", "filter", "remove"])
                subprocess.run(["pktmon", "filter", "add", "Ping", "-t", "ICMP"])
                print("Monitoring...\n\n")
                try:
                    subprocess.run(["pktmon", "start", "-c", "-m", "real-time"])
                except KeyboardInterrupt:
                    pass
            if command == "ftp":
                subprocess.run(["pktmon", "filter", "remove"])
                subprocess.run(["pktmon", "filter", "add", "FTP", "-t", "TCP", "-p", "21"])
                print("Monitoring...\n\n")
                try:
                    subprocess.run(["pktmon", "start", "-c", "-m", "real-time"])
                except KeyboardInterrupt:
                    pass
            if command == "telnet":
                subprocess.run(["pktmon", "filter", "remove"])
                subprocess.run(["pktmon", "filter", "add", "Telnet", "-t", "TCP", "-p", "23"])
                print("Monitoring...\n\n")
                try:
                    subprocess.run(["pktmon", "start", "-c", "-m", "real-time"])
                except KeyboardInterrupt:
                    pass
            if command == "dns":
                subprocess.run(["pktmon", "filter", "remove"])
                subprocess.run(["pktmon", "filter", "add", "DnsTraffic", "-t", "UDP", "-p", "53"])
                print("Monitoring...\n\n")
                try:
                    subprocess.run(["pktmon", "start", "-c", "-m", "real-time"])
                except KeyboardInterrupt:
                    pass
            if command == "tcp":
                subprocess.run(["pktmon", "filter", "remove"])
                subprocess.run(["pktmon", "filter", "add", "WebTraffic", "-t", "TCP", "-p", "443", "-d", "IPv4"])
                subprocess.run(["pktmon", "filter", "add", "WebTraffic", "-t", "TCP", "-p", "80", "-d", "IPv4"])
                print("Monitoring...\n\n")
                try:
                    subprocess.run(["pktmon", "start", "-c", "-m", "real-time"])
                except KeyboardInterrupt:
                    pass
            if command == "device":
                subprocess.run(["pktmon", "filter", "remove"])
                device = input("\nEnter device number (default: all)? ")
                if not device:
                    device = "all"
                print("Monitoring device " + device + "...\n\n")
                try:
                    subprocess.run(["pktmon", "start", "-c", "--trace",
                                    "-p", "Microsoft-Windows-TCPIP", "--comp", device,
                                    "-m", "real-time"])
                except KeyboardInterrupt:
                    pass
            elif command == "list":
                print("Listing devices...\n\n")
                subprocess.run(["pktmon", "list"])
            elif command == "exit":
                return
            else:
                pass
    except KeyboardInterrupt:
        print("\nStopping packet monitoring...\n\n")


if __name__ != "__main__":
    pass
else:
    _main()
